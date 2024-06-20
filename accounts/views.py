from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from blog.models import Comment
from .forms import ProfileUpdateForm, UserUpdateForm
from .models import Profile


@login_required
def user_profile(request, username):
    """
    Display a user's profile page.
    Fetches the user's profile, comments, and checks if the current user
    is viewing their own profile.
    **Context:**
    ``profile``
        An instance of :model:`accounts.Profile`.
    ``is_current_user``
        A boolean indicating if the profile belongs to the current user.
    ``comments``
        A queryset of :model:`blog.Comment` instances made by the user.
    **Template:**
    :template:`accounts/user_profile.html`
    Args:
        request: The HTTP request object.
        username: The username of the user whose profile is to be displayed.
    Returns:
        HttpResponse: The rendered user profile page.
    """
    user = get_object_or_404(User, username=username)
    profile = user.profile
    comments = Comment.objects.filter(user=user)
    is_current_user = request.user == user

    context = {
        "profile": profile,
        "is_current_user": is_current_user,
        "comments": comments,
    }
    return render(request, "accounts/user_profile.html", context)


@login_required
def update_profile(request):
    """
    Update the current user's profile.
    Handles the submission of profile and user update forms, and updates
    the user's profile and account information.
    **Context:**
    ``user_form``
        An instance of :form:`accounts.UserUpdateForm`.
    ``profile_form``
        An instance of :form:`accounts.ProfileUpdateForm`.
    **Template:**
    :template:`accounts/update_profile.html`
    Args:
        request: The HTTP request object.
    Returns:
        HttpResponse: The rendered update profile page or a
        redirect to the user profile page on success.
    """
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
    """
    Delete the current user's account.
    Processes POST requests to delete the user's
    account and redirects to the home page.
    Raises a 404 error for non-POST requests.
    Args:
        request: The HTTP request object.
    Returns:
        HttpResponse: A redirect to the home page on successful deletion.
        Http404: If the request method is not POST.
    """
    if request.method == "POST":
        request.user.delete()
        messages.success(request, "Your account has been successfully deleted")
        return redirect("home")
    else:
        # This ensures the view only processes POST requests
        raise Http404
