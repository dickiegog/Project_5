from django.shortcuts import render
from .models import Product, Category

def product_catalog(request):
    """View to display all products with filtering, searching, and sorting."""
    query = request.GET.get('q', None)
    category_name = request.GET.get('category', None)
    sort_by = request.GET.get('sort', None)
    categories = Category.objects.all()

    products = Product.objects.all()

    if category_name:
        products = products.filter(category__name=category_name)

    if query:
        products = products.filter(name__icontains=query)

    if sort_by:
        if sort_by == 'price_asc':
            products = products.order_by('price')
        elif sort_by == 'price_desc':
            products = products.order_by('-price')

    return render(request, 'products/catalog.html', {
        'products': products,
        'categories': categories,
        'selected_category': category_name,
        'query': query,
        'sort_by': sort_by,
    })
