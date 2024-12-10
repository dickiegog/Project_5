from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm

@login_required
def edit_profile(request):
    """Allow logged-in users to edit their profile."""
    profile = UserProfile.objects.get(user=request.user)
    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("edit_profile")
    else:
        form = UserProfileForm(instance=profile)
    context = {"form": form}
    return render(request, "profiles/edit_profile.html", context)
