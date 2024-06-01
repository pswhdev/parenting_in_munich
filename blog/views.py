from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post, Category


# Create your views here.


class PostList(generic.ListView):
    """
    View to list all posts with a published status.
    **Template:**
    :template:`blog/posts.html`
    """

    # Only include published posts
    queryset = Post.objects.filter(status=1)
    template_name = "blog/posts.html"
    paginate_by = 6

    def get_context_data(self, **kwargs):
        """
        Add categories to the context to be used by the template.
        **Context:**
        ``categories``
        A queryset of all categories.
        """

        # Get the existing context data from the parent class
        context = super().get_context_data(**kwargs)
        # Add all categories to the context
        context["categories"] = Category.objects.all()
        return context


def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.
    **Context**
    ``post``
    An instance of :model:`blog.Post`.
    **Template:**
    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    # Get the post or return 404
    post = get_object_or_404(queryset, slug=slug)
    categories = Category.objects.all()

    return render(
        request,
        "blog/post_detail.html",
        {"post": post, "categories": categories},
    )


def category_posts(request, category_id):
    """
    Display posts belonging to a specific category.
    **Context:**
    ``category``
        An instance of :model:`blog.Category`.
    ``posts``
        A queryset of all posts in the category.
    ``categories``
        A queryset of all categories.
    **Template:**
    :template:`blog/category_posts.html`
    """
    category = get_object_or_404(Category, id=category_id)
    # Get all published posts in the category
    posts = Post.objects.filter(category=category, status=1)
    categories = Category.objects.all()

    return render(request, 'blog/category_posts.html', {'category': category, 'posts': posts, 'categories': categories})
