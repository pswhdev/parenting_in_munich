from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import ContactUsForm


def about_site(request):
    """
    Renders the About page
    """
    if request.method == "POST":
        contact_form = ContactUsForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Your message has been "
                "successfully submitted. We will and get back to "
                "you as soon as possible.",
            )
    about = About.objects.all().order_by("-updated_on").first()
    contact_us_form = ContactUsForm()

    return render(
        request,
        "about/about.html",
        {"about": about, "contact_us_form": contact_us_form},
    )
