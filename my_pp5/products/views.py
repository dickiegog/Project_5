from django.shortcuts import render
from .models import Product

def product_catalog(request):
    """View to display all products."""
    products = Product.objects.all()
    return render(request, 'products/catalog.html', {'products': products})
