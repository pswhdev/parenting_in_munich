from django.urls import path
from . import views


urlpatterns = [
    path("", views.Homepage.as_view(), name="home"),
    path("site-rules/", views.site_rules, name="site_rules"),
    path("restricted-area/", views.restricted_area, name="restricted_area")
]
