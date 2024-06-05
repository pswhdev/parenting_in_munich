from django.core.paginator import Paginator
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
        context = super().get_context_data(**kwargs)
        context["category"] = Category.objects.first()  # Fetch any specific category
        return context


def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.
    **Context**
    ``post``
    An instance of :model:`blog.Post`.
    ``category``
    An instance of :model:`blog.Category` associated with the post.
    **Template:**
    :template:`blog/post_detail.html`
    """
    # Fetch the post object
    post = get_object_or_404(Post, slug=slug, status=1)

    # Get the category associated with the post
    category = post.category

    return render(
        request,
        "blog/post_detail.html",
        {"post": post, "category": category},
    )


def category_posts(request, category_slug):
    """
    Display posts belonging to a specific category.
    **Context:**
    ``category``
        An instance of :model:`blog.Category`.
    ``posts``
        A queryset of all posts in the category.
    **Template:**
    :template:`blog/category_posts.html`
    """
    category = get_object_or_404(Category, slug=category_slug)
    posts = Post.objects.filter(category=category, status=1)
    # Show 6 posts per page
    paginator = Paginator(posts, 6)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/category_posts.html', {
        'category': category,
        'page_obj': page_obj,
        'is_paginated': page_obj.has_other_pages()
    })
