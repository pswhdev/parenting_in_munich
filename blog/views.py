from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, reverse
from django.views import generic
from django.contrib import messages
from .forms import CommentForm
from .models import Category, Comment, Post


class PostList(generic.ListView):
    """
    View to list all posts with a published status.
    **Template:**
    :template:`blog/posts.html`
    """
    model = Post
    # Only include published posts
    queryset = Post.objects.filter(status=1)
    template_name = "blog/posts.html"
    paginate_by = 6

    def get_context_data(self, **kwargs):
        """Get the context for this view."""
        context = super().get_context_data(**kwargs)
        # Fetch any specific category
        context["categories"] = Category.objects.all()
        # Indicate if there are no posts found
        context["no_posts"] = not self.get_queryset().exists()
        # To include search results
        context["search_query"] = self.request.GET.get('q', '')
        return context

    def get_queryset(self):
        """Return the list of items for this view."""
        query = self.request.GET.get('q')
        if query:
            return Post.objects.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query),
                status=1
            )
        return Post.objects.filter(status=1)


def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.
    **Context**
    ``post``
        An instance of :model:`blog.Post`.
    ``category``
        An instance of :model:`blog.Category` associated with the post.
    ``comments``
        A queryset of all comments related to the post.
    ``comment_count``
        The number of approved comments for the post.
    ``comment_form``
        An instance of :form:`blog.CommentForm`.
    **Template:**
    :template:`blog/post_detail.html`
    """

    # Fetch the post object
    post = get_object_or_404(Post, slug=slug, status=1)

    # Get the category associated with the post
    category = post.category
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                "Comment submitted and awaiting approval."
            )
            return HttpResponseRedirect(reverse('post_detail', args=[slug]))
        else:
            messages.add_message(
                request, messages.ERROR,
                "There was an error submitting your comment. "
                "Please correct the errors below."
            )
    else:
        comment_form = CommentForm()

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "category": category,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )


def category_posts(request, category_slug):
    """
    Display posts belonging to a specific category.
    **Context:**
    ``category``
        An instance of :model:`blog.Category`.
    ``page_obj``
        A paginator page object containing the posts.
    ``is_paginated``
        A boolean indicating if pagination is applied.
    **Template:**
    :template:`blog/category_posts.html`
    """
    category = get_object_or_404(Category, slug=category_slug)
    posts = Post.objects.filter(category=category, status=1)
    # Show 6 posts per page
    paginator = Paginator(posts, 6)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "blog/category_posts.html",
        {
            "category": category,
            "page_obj": page_obj,
            "is_paginated": page_obj.has_other_pages(),
        },
    )


def comment_edit(request, slug, comment_id):
    """
    View to edit comments.
    Args:
        request: The HTTP request object.
        slug: The slug of the post the comment belongs to.
        comment_id: The ID of the comment to be edited.
    Returns:
        HttpResponseRedirect: Redirects to the post detail page.
    """
    if request.method == "POST":
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.user == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, "Comment Updated!")
        else:
            messages.add_message(
                request, messages.ERROR, "Error updating comment!"
            )

    return HttpResponseRedirect(reverse("post_detail", args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    View to delete comments.
    Args:
        request: The HTTP request object.
        slug: The slug of the post the comment belongs to.
        comment_id: The ID of the comment to be deleted.
    Returns:
        HttpResponseRedirect: Redirects to the post detail page.
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.user == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, "Comment deleted!")
    else:
        messages.add_message(
            request, messages.ERROR, "You can only delete your own comments!"
        )

    return HttpResponseRedirect(reverse("post_detail", args=[slug]))
