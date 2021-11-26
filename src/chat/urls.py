from django.urls import path
from . import views


app_name = 'chat'


urlpatterns = [
    path('', views.index, name='index'),
    path('user-login/', views.api_login_user, name="user_login"),
    path('user-signup/', views.api_signup_user, name="user_signup"),
    path('user-logout/', views.api_logout_user, name="user_logout"),
    path('post-message/', views.post_user_message, name='post_message'),
]
