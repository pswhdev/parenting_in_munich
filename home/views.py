from django.shortcuts import render
from django.views.generic import TemplateView


class Homepage(TemplateView):
    """
    View to render the homepage.
    **Template:**
    :template:`home/index.html`
    """
    template_name = 'home/index.html'


def site_rules(request):
    """
    Display the site rules page.
    **Template:**
    :template:`home/site_rules.html`
    Args:
        request: The HTTP request object.
    Returns:
        HttpResponse: The rendered site rules page.
    """
    return render(request, 'home/site_rules.html')


def custom_404_view(request, exception):
    """
    Custom 404 error view.
    This view renders a custom 404 error page when a page is not found.
    **Template:**
    :template:`404.html`
    Args:
        request: The HTTP request object.
        exception: The exception that triggered the 404 error.
    Returns:
        HttpResponse: The rendered 404 error page with a 404 status code.
    """
    return render(request, '404.html', status=404)

def restricted_area(request):
    """
    Display the restricted area page.
    This view renders a page indicating a restricted area, accessible
    regardless of user authentication status.
    **Template:**
    :template:`home/restricted_area.html`
    Args:
        request: The HTTP request object.
    Returns:
        HttpResponse: The rendered restricted area page.
    """
    return render(request, "home/restricted_area.html")
