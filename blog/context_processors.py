from .models import Category


def categories(request):
    """
    Context processor function to add categories to the context.
    This function retrieves all Category objects and adds them to the context
    dictionary, making them available in templates.
    Args:
        request: The HTTP request object.
    Returns:
        dict: A dictionary containing all
        categories under the key 'categories'.
    """
    return {
        'categories': Category.objects.all()
    }
