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

    context = {
        'user_form': user_form,
        'form': profile_form,
    }
    return render(request, 'profiles/edit_profile.html', {
    'user_form': user_form,
    'profile_form': profile_form,
})

