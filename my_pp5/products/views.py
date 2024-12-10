from django.shortcuts import render
from .models import Product, Category

def product_catalog(request):
    """View to display all products with category filtering and search."""
    query = request.GET.get('q', None)
    category_name = request.GET.get('category', None)
    categories = Category.objects.all()

    products = Product.objects.all()

    if category_name:
        products = products.filter(category__name=category_name)

    if query:
        products = products.filter(name__icontains=query)

    return render(request, 'products/catalog.html', {
        'products': products,
        'categories': categories,
        'selected_category': category_name,
        'query': query,
    })
