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

    return render(
        request,
        "blog/post_detail.html",
        {"post": post},
    )

def category_posts(request, category_id):
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
    category = get_object_or_404(Category, id=category_id)
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
