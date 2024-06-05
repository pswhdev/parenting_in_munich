from . import views
from django.urls import path

urlpatterns = [
    # Posts page listing all posts
    path('', views.PostList.as_view(), name='posts'),
    # Detail page for an individual post
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    # Posts by category
    path('category/<slug:category_slug>/', views.category_posts, name='category_posts'),
]
