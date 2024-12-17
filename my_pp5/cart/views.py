from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, CartItem
from products.models import Product
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    cart, _ = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not created:
        cart_item.quantity += 1
        messages.info(request, f"Quantity of '{product.name}' increased in your cart.")
    else:
        cart_item.quantity = 1
        messages.success(request, f"'{product.name}' was added to your cart!")

    cart_item.save()
    return redirect('cart:cart_detail')

def cart_detail(request):
    """View to display the cart details."""
    cart, _ = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.items.all()  # Fetch the related CartItem objects
    return render(request, 'cart/cart_detail.html', {'cart': cart, 'cart_items': cart_items})

    from django.views.decorators.http import require_POST

@require_POST
def update_cart_item(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    new_quantity = int(request.POST.get('quantity', 1))
    if new_quantity > 0:
        cart_item.quantity = new_quantity
        cart_item.save()
        messages.success(request, f"Quantity updated to {new_quantity} for '{cart_item.product.name}'.")
    else:
        cart_item.delete()
        messages.warning(request, f"'{cart_item.product.name}' was removed from your cart as quantity was set to 0.")
    return redirect('cart:cart_detail')

    
@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)

    if cart_item.cart.user == request.user:
        product_name = cart_item.product.name
        cart_item.delete()
        messages.success(request, f"'{product_name}' was removed from your cart.")
    return redirect('cart:cart_detail')

def checkout(request):
    """Placeholder view for the checkout process."""
    return HttpResponse("Checkout page coming soon!")
