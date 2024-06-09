"""
URL configuration for parenting_website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from home import views
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404

urlpatterns = [
    path("about/", include("about.urls"), name="about-urls"),
    path("accounts/", include("allauth.urls")),
    path("admin/", admin.site.urls),
    path("summernote/", include("django_summernote.urls")),
    path("", include("home.urls")),
    path("posts/", include("blog.urls"), name="blog-urls"),
    path("user_profiles/", include("accounts.urls", namespace="user_profiles")),
    path("events/", include('events.urls')),
    path('useful_links/', include('useful_links.urls')),
]

handler404 = views.custom_404_view
