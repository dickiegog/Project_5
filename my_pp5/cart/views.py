from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, CartItem
from products.models import Product
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # Get or create the cart for the user
    cart, _ = Cart.objects.get_or_create(user=request.user)

    # Get or create the cart item
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    # If the item already exists, increment the quantity
    if not created:
        cart_item.quantity += 1
    else:
        cart_item.quantity = 1  # Start with 1 for new items

    # Save the cart item
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
    else:
        cart_item.delete()
    return redirect('cart:cart_detail')

    
@login_required
def remove_from_cart(request, item_id):
    """Remove a specific item from the cart."""
    cart_item = get_object_or_404(CartItem, id=item_id)

    # Only allow users to remove their own cart items
    if cart_item.cart.user == request.user:
        cart_item.delete()

    return redirect('cart:cart_detail')

def checkout(request):
    """Placeholder view for the checkout process."""
    return HttpResponse("Checkout page coming soon!")
