from django.shortcuts import render

def checkout(request):
    """Render the checkout page."""
    return render(request, 'checkout/checkout.html')
