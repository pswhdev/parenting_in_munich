from django.urls import path
from . import views

# To insure uniqueness and avoid conflicts
app_name = 'userinfo'

urlpatterns = [
    path('profile/update/', views.update_profile, name='update_profile'),
    path('profile/<str:username>/', views.user_profile, name='user_profile'),
    path('delete_account/', views.delete_account, name='delete_account'),
]
