from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('delete_account/', views.delete_account, name='delete_account'),
]
