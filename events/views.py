from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Event


@login_required
def events(request):
    events_list = Event.objects.all()
    return render(request, 'events/events.html', {'events': events_list})


def restricted_area(request):
    return render(request, 'events/restricted_area.html')
