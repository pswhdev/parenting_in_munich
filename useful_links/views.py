from django.shortcuts import render
from .models import Topic

def useful_links(request):
    topics = Topic.objects.prefetch_related('links').all()
    return render(request, 'useful_links/useful_links.html', {'topics': topics})
