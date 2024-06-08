from django.urls import path
from .views import useful_links

urlpatterns = [
    path("", useful_links, name="useful_links"),
]
