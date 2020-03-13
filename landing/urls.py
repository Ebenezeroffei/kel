from django.urls import path
from . import views as landing_views

app_name = 'landing'
urlpatterns = [
    path('',landing_views.HomeView.as_view(),name = 'home'),
]