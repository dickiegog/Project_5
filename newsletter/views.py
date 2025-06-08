from django.shortcuts import redirect
from django.contrib import messages
from .models import Newsletter

def newsletter_signup(request):
    if request.method == "POST":
        email = request.POST.get("email")
        if email:
            Newsletter.objects.get_or_create(email=email)
            messages.success(request, "Thank you for subscribing to our newsletter!")
        else:
            messages.error(request, "Please enter a valid email address.")
        return redirect("home")
