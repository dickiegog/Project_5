from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm, UserUpdateForm
from .models import UserProfile
from django.contrib import messages

@login_required
def edit_profile(request):
    """Edit user and profile details."""
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=user_profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Your profile has been updated successfully!")
            return redirect('profiles:edit_profile')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = UserProfileForm(instance=user_profile)

    return render(request, 'profiles/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })

@login_required
def save_profile_data(request):
    """Save missing profile data to the user's profile."""
    if request.method == 'POST':
        profile, created = UserProfile.objects.get_or_create(user=request.user)

        # Validate and update fields
        valid_fields = ['address', 'city', 'postal_code', 'phone_number', 'country']
        for field in valid_fields:
            value = request.POST.get(field)
            if value:
                setattr(profile, field, value)

        profile.save()
        messages.success(request, "Your profile has been updated successfully!")
        return redirect('profiles:edit_profile')

    return redirect('profiles:edit_profile')
