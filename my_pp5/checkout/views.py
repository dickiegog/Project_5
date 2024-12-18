from django.shortcuts import render, redirect
from .forms import CheckoutForm
from cart.models import CartItem
from .models import Order, OrderItem
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def checkout(request):
    """Process the checkout form and display cart items."""
    cart_items = CartItem.objects.filter(cart__user=request.user)
    if not cart_items:
        messages.info(request, "Your cart is empty. Add items before checking out.")
        return redirect('cart:cart_detail')

    form = CheckoutForm()
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # Create the order
            order = form.save(commit=False)
            order.user = request.user
            order.total = sum(item.product.price * item.quantity for item in cart_items)
            order.save()

            # Create order items
            for item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity,
                    price=item.product.price
                )
            # Clear the cart
            cart_items.delete()
            messages.success(request, "Your order has been placed successfully!")
            return redirect('checkout:success')

    return render(request, 'checkout/checkout.html', {'form': form, 'cart_items': cart_items})

@login_required
def success(request):
    """Display order success message."""
    return render(request, 'checkout/success.html')
