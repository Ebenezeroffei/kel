from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from . import views as user_views


app_name = 'user'
urlpatterns = [
    path('signin/',LoginView.as_view(template_name = 'user/signin.html'),name = 'signin'),
    path('signup/',user_views.NewUserView.as_view(template_name = 'user/signup.html'),name = 'signup'),
]