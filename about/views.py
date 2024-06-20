from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import ContactUsForm
from .models import About


def about_site(request):
    """
    Render the About page.
    Handles both GET and POST requests.
    For GET requests, it initializes an empty contact form.
    For POST requests, it processes the submitted contact form, validates it,
    and either saves the data and displays a success message,
    or displays an error message if the form is invalid.
    Args:
        request: The HTTP request object.
    Returns:
        HttpResponse: The rendered about page with the latest about information
        and the contact form.
    """
    if request.method == "POST":
        contact_us_form = ContactUsForm(data=request.POST)
        if contact_us_form.is_valid():
            contact_us_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Your message has been successfully submitted. "
                "We will get in touch with you soon.",
            )
            # Redirect to the about page to clear the form
            return redirect('about')
        else:
            messages.add_message(
                request,
                messages.ERROR,
                "There was an error submitting your message. "
                "Please correct the errors below.",
            )
    else:
        contact_us_form = ContactUsForm()

    about = About.objects.all().order_by("-updated_on").first()

    return render(
        request,
        "about/about.html",
        {"about": about, "contact_us_form": contact_us_form},
    )
