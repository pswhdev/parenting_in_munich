from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserUpdateForm, ProfileUpdateForm
from .models import Profile


@login_required
def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    profile = user.profile
    is_current_user = request.user == user

    context = {"profile": profile, "is_current_user": is_current_user}
    return render(request, "accounts/user_profile.html", context)


@login_required
def update_profile(request):
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile
        )
        if user_form.is_valid() and profile_form.is_valid():
            profile = profile_form.save(commit=False)
            custom_location = profile_form.cleaned_data.get("custom_location")
            if profile.location == "Others" and custom_location:
                profile.location = custom_location
            profile.save()
            user_form.save()
            messages.success(request, "Your profile has been updated!")
            return redirect(
                "userinfo:user_profile", username=request.user.username
            )
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        "user_form": user_form,
        "profile_form": profile_form,
    }
    return render(request, "accounts/update_profile.html", context)


@login_required
def delete_account(request):
    if request.method == "POST":
        request.user.delete()
        messages.success(request, "Your account has been deleted.")
        return redirect("home")
    return render(request, "accounts/delete_account.html")
