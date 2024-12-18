from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm, UserUpdateForm
from .models import UserProfile
from django.contrib import messages

@login_required
def edit_profile(request):
    """View to edit user profile."""
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
            messages.error(request, "There was an error updating your profile. Please try again.")
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = UserProfileForm(instance=user_profile)

    return render(request, 'profiles/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })
2
@login_required
def save_profile(request):
    """Save checkout data to the user's profile."""
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        address = request.POST.get('address')
        city = request.POST.get('city')
        postal_code = request.POST.get('postal_code')
        phone_number = request.POST.get('phone_number')

        # Split full_name into first and last name
        first_name, last_name = full_name.split(' ', 1) if ' ' in full_name else (full_name, '')

        # Update User fields
        request.user.first_name = first_name
        request.user.last_name = last_name
        request.user.save()

        # Update UserProfile fields
        profile, created = UserProfile.objects.get_or_create(user=request.user)
        profile.address = address
        profile.city = city
        profile.postal_code = postal_code
        profile.phone_number = phone_number
        profile.save()

        messages.success(request, "Your information has been saved to your profile!")
    return redirect('checkout:success')
