from django.urls import path
from . import views

urlpatterns = [
    path("", views.events, name="events"),
    path("restricted-area/", views.restricted_area, name="restricted_area"),
]
