from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Product, Category
from .forms import ProductForm

def is_superuser(user):
    return user.is_superuser

@login_required
@user_passes_test(is_superuser)
def add_product(request):
    """Allow superusers to add a product."""
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Product added successfully!")
            return redirect('products:add_product')
        else:
            messages.error(request, "Failed to add product. Please check the form.")
    else:
        form = ProductForm()

    return render(request, 'products/add_product.html', {'form': form})

@login_required
@user_passes_test(is_superuser)
def update_product(request, product_id):
    """Allow superusers to update a product."""
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Product updated successfully!")
            return redirect('products:product_catalog')  # Redirect to the catalog page
        else:
            messages.error(request, "Failed to update product. Please check the form.")
    else:
        form = ProductForm(instance=product)

    return render(request, 'products/update_product.html', {'form': form, 'product': product})

@login_required
@user_passes_test(is_superuser)
def delete_product(request, product_id):
    """Allow superusers to delete a product."""
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    messages.success(request, "Product deleted successfully!")
    return redirect('products:product_catalog')

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
