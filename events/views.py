from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Event


@login_required
def events(request):
    """
    Display a list of upcoming events.
    This view is accessible only to logged-in users. It fetches all events
    whose end date is greater than or equal to today's date, ordered by the
    start date.
    **Context:**
    ``events``
        A queryset of :model:`events.Event` instances.
    **Template:**
    :template:`events/events.html`
    Args:
        request: The HTTP request object.
    Returns:
        HttpResponse: The rendered events page.
    """
    today = timezone.now().date()
    events_list = Event.objects.filter(
        end_date__gte=today).order_by("start_date")
    return render(request, "events/events.html", {"events": events_list})


def restricted_area(request):
    """
    Display the restricted area page.
    This view renders a page indicating a restricted area, accessible
    regardless of user authentication status.
    **Template:**
    :template:`events/restricted_area.html`
    Args:
        request: The HTTP request object.
    Returns:
        HttpResponse: The rendered restricted area page.
    """
    return render(request, "events/restricted_area.html")
