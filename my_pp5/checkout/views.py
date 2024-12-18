from django.shortcuts import render, redirect
from .forms import CheckoutForm
from cart.models import CartItem
from .models import Order, OrderItem
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from profiles.models import UserProfile
from django.views.decorators.csrf import csrf_exempt

@login_required
def checkout(request):
    """Process the checkout form and display cart items."""
    cart_items = CartItem.objects.filter(cart__user=request.user)
    if not cart_items:
        messages.info(request, "Your cart is empty. Add items before checking out.")
        return redirect('cart:cart_detail')

    # Retrieve or create the user's profile
    profile, created = UserProfile.objects.get_or_create(user=request.user)

    # Pre-fill the form with profile data
    initial_data = {
        'full_name': f"{request.user.first_name} {request.user.last_name}",
        'address': profile.address,
        'city': profile.city,
        'postal_code': profile.postal_code,
        'phone_number': profile.phone_number,
    }

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.total = sum(item.product.price * item.quantity for item in cart_items)
            order.save()

            for item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity,
                    price=item.product.price
                )
            cart_items.delete()

            # Check for missing profile data
            missing_fields = []
            for field in ['address', 'city', 'postal_code', 'phone_number']:
                if not getattr(profile, field):
                    missing_fields.append(field)

            if missing_fields:
                # Store missing data in session
                request.session['missing_profile_data'] = {
                    field: form.cleaned_data[field] for field in missing_fields
                }
                return redirect('checkout:success')
            else:
                messages.success(request, "Your order has been placed successfully!")
                return redirect('checkout:success')
    else:
        form = CheckoutForm(initial=initial_data)

    return render(request, 'checkout/checkout.html', {
        'form': form,
        'cart_items': cart_items,
    })

@login_required
def success(request):
    """Display order success message and optionally save profile data."""
    save_profile_data = request.session.pop('save_profile_data', None)
    missing_profile_data = []

    if save_profile_data:
        for field, value in save_profile_data.items():
            missing_profile_data.append({'field': field, 'value': value})

    return render(request, 'checkout/success.html', {
        'missing_profile_data': missing_profile_data,
    })

    return render(request, 'checkout/success.html')


@login_required
def save_profile(request):
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
