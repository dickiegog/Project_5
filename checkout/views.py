import stripe
import json
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.urls import reverse
from .forms import CheckoutForm
from .models import Order, OrderItem
from cart.models import CartItem
from profiles.models import UserProfile

stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def checkout(request):
    cart_items = CartItem.objects.filter(cart__user=request.user)
    if not cart_items:
        messages.info(request, "Your cart is empty. Add items before checking out.")
        return redirect('cart:cart_detail')

    profile, _ = UserProfile.objects.get_or_create(user=request.user)

    # Pre-fill form with profile data
    initial_data = {
        'full_name': f"{request.user.first_name} {request.user.last_name}",
        'email': request.user.email, 
        'address': profile.address,
        'city': profile.city,
        'postal_code': profile.postal_code,
        'phone_number': profile.phone_number,
        'country': profile.country
    }
    form = CheckoutForm(initial=initial_data)
    return render(request, 'checkout/checkout.html', {
        'form': form,
        'cart_items': cart_items,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
    })

@login_required
def success(request):
    if 'cart' in request.session:
        del request.session['cart']
    CartItem.objects.filter(cart__user=request.user).delete()

    messages.success(request, "Payment successful! Thank you for your order.")

    missing_profile_data = request.session.pop('missing_profile_data', {})
    missing_fields = [
        field for field in ['address', 'city', 'postal_code', 'phone_number', 'country']
        if field not in missing_profile_data
    ]

    return render(request, 'checkout/success.html', {
        'missing_profile_data': missing_profile_data,
        'missing_fields': missing_fields,
    })

@login_required
def save_profile_data(request):
    """Save missing profile data from the checkout form."""
    if request.method == 'POST':
        profile, created = UserProfile.objects.get_or_create(user=request.user)

        profile.address = request.POST.get('address') or profile.address
        profile.city = request.POST.get('city') or profile.city
        profile.postal_code = request.POST.get('postal_code') or profile.postal_code
        profile.phone_number = request.POST.get('phone_number') or profile.phone_number
        profile.save()

        messages.success(request, "Your profile has been updated successfully!")
        return redirect('profiles:edit_profile')

    return redirect('profiles:edit_profile')

@csrf_exempt
@login_required
def create_checkout_session(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            cart_items = CartItem.objects.filter(cart__user=request.user)
            if not cart_items:
                return JsonResponse({'error': 'Your cart is empty!'}, status=400)

            order = Order.objects.create(
                user=request.user,
                full_name=data.get('full_name'),
                email=data.get('email'),
                address=data.get('address'),
                city=data.get('city'),
                postal_code=data.get('postal_code'),
                phone=data.get('phone_number'),
                country=data.get('country'),
                total=sum(item.product.price * item.quantity for item in cart_items),
                status='pending'
            )

            for item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity,
                    price=item.product.price,
                )

            line_items = [
                {
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {'name': item.product.name},
                        'unit_amount': int(item.product.price * 100),
                    },
                    'quantity': item.quantity,
                }
                for item in cart_items
            ]

            cart_items.delete()  # Move this AFTER building line_items
            request.session['order_id'] = order.id

            YOUR_DOMAIN = f"{request.scheme}://{request.get_host()}"
            success_url = YOUR_DOMAIN + reverse('checkout:success')
            cancel_url = YOUR_DOMAIN + reverse('checkout:checkout')

            checkout_session = stripe.checkout.Session.create(
                payment_method_types=["card"],
                line_items=line_items,
                mode="payment",
                success_url=success_url,
                cancel_url=cancel_url,
            )
            return JsonResponse({"id": checkout_session.id})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)