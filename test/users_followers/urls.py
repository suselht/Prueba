from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.get_all_users_followers, name='get_all_users_followers'),
    path('user/fewest_followers/', views.user_with_fewest_followers, name='user_with_fewest_followers'),
]