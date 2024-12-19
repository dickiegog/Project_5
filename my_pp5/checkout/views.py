import stripe
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .forms import CheckoutForm
from .models import Order, OrderItem
from cart.models import CartItem
from profiles.models import UserProfile

stripe.api_key = settings.STRIPE_SECRET_KEY


@login_required
def checkout(request):
    """Render the checkout page."""
    cart_items = CartItem.objects.filter(cart__user=request.user)
    if not cart_items:
        messages.info(request, "Your cart is empty. Add items before checking out.")
        return redirect('cart:cart_detail')

    profile, _ = UserProfile.objects.get_or_create(user=request.user)

    # Pre-fill form with profile data
    initial_data = {
        'full_name': f"{request.user.first_name} {request.user.last_name}",
        'address': profile.address,
        'city': profile.city,
        'postal_code': profile.postal_code,
        'phone_number': profile.phone_number,
    }

    form = CheckoutForm(initial=initial_data)
    return render(request, 'checkout/checkout.html', {
        'form': form,
        'cart_items': cart_items,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,  # Pass Stripe public key
    })

@login_required
def success(request):
    """
    Display the order success page and handle missing profile data.
    """
    # Fetch any missing profile data stored in the session
    missing_profile_data = request.session.pop('missing_profile_data', {})

    # Ensure the data is a dictionary to prevent template errors
    if not isinstance(missing_profile_data, dict):
        missing_profile_data = {}

    # Render the template and pass missing profile data
    return render(request, 'checkout/success.html', {
        'missing_profile_data': missing_profile_data
    })

@login_required
def save_profile_data(request):
    """Save missing profile data from the checkout form."""
    if request.method == 'POST':
        profile, created = UserProfile.objects.get_or_create(user=request.user)

        # Update only missing fields
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
    """Create a Stripe Checkout session."""
    try:
        cart_items = CartItem.objects.filter(cart__user=request.user)
        if not cart_items:
            return JsonResponse({'error': 'Your cart is empty!'}, status=400)

        line_items = []
        for item in cart_items:
            line_items.append({
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': item.product.name,
                    },
                    'unit_amount': int(item.product.price * 100),  # Stripe expects cents
                },
                'quantity': item.quantity,
            })

        YOUR_DOMAIN = "http://8000-dickiegog-project5-ljqxmw7dt1f.ws-eu117.gitpod.io"
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=line_items,
            mode="payment",
            success_url=f"{YOUR_DOMAIN}/checkout/success/",
            cancel_url=f"{YOUR_DOMAIN}/checkout/",
        )
        return JsonResponse({"id": checkout_session.id})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

    """Create a Stripe Checkout session."""
    try:
        cart_items = CartItem.objects.filter(cart__user=request.user)
        if not cart_items:
            return JsonResponse({'error': 'Your cart is empty!'}, status=400)

        line_items = []
        for item in cart_items:
            line_items.append({
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': item.product.name,
                    },
                    'unit_amount': int(item.product.price * 100),  # Price in cents
                },
                'quantity': item.quantity,
            })

        YOUR_DOMAIN = "http://8000-dickiegog-project5-ljqxmw7dt1f.ws-eu117.gitpod.io"
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=line_items,
            mode="payment",
            success_url=f"{YOUR_DOMAIN}/checkout/success/",
            cancel_url=f"{YOUR_DOMAIN}/checkout/",
        )
        return JsonResponse({"id": checkout_session.id})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)