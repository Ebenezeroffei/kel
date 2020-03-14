from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView

app_name = 'user'
urlpatterns = [
    path('signin/',LoginView.as_view(template_name = 'user/signin.html'),name = 'signin'),
]