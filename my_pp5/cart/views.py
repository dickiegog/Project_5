from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, CartItem
from products.models import Product

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart:cart_detail')

def cart_detail(request):
    """View to display the cart details."""
    cart, _ = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.items.all()  # Fetch the related CartItem objects
    return render(request, 'cart/cart_detail.html', {'cart': cart, 'cart_items': cart_items})
    
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()
    return redirect('cart:cart_detail')
