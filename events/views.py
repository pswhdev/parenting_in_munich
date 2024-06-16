from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Event


@login_required
def events(request):
    today = timezone.now().date()
    events_list = Event.objects.filter(
        end_date__gte=today).order_by("start_date")
    return render(request, "events/events.html", {"events": events_list})


def restricted_area(request):
    return render(request, "events/restricted_area.html")
