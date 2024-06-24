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


def custom_403_view(request, exception):
    """
    Custom handler for 403 Forbidden errors.

    This function renders a custom 403 error page when a 403 Forbidden error
    occurs. It uses the Django `render` function to display the '403.html'
    template with a status code of 403.
    Args:
        request: HttpRequest object that represents the request that
        triggered the 403 error.
        exception: The exception that triggered the 403 error.
    Returns:
        HttpResponse: A response object containing the rendered 403 error
        page with a 403 status code.
    """
    return render(request, '403.html', status=403)


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
