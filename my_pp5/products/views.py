from django.shortcuts import render
from .models import Product, Category

def product_catalog(request):
    """View to display all products with category filtering."""
    category_name = request.GET.get('category', None)
    categories = Category.objects.all()

    if category_name:
        products = Product.objects.filter(category__name=category_name)
    else:
        products = Product.objects.all()

    return render(request, 'products/catalog.html', {
        'products': products,
        'categories': categories,
        'selected_category': category_name,
    })
