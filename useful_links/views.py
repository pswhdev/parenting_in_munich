from django.shortcuts import render
from .models import Topic


def useful_links(request):
    """
    Display a list of topics and their associated links.
    This view fetches all topics along with their related links and renders
    them on the useful links page.
    **Context:**
    ``topics``
        A queryset of :model:`useful_links.Topic` instances, each with its
        related links prefetched.
    **Template:**
    :template:`useful_links/useful_links.html`
    Args:
        request: The HTTP request object.
    Returns:
        HttpResponse: The rendered useful links page.
    """
    topics = Topic.objects.prefetch_related('links').all()
    return render(
        request, 'useful_links/useful_links.html', {'topics': topics}
    )
