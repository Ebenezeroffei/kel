from django.urls import path
from . import views as landing_views

app_name = 'landing'
urlpatterns = [
    path('',landing_views.ProductListView.as_view(),name = 'home'),
    path('product/<int:pk>/',landing_views.ProductDetailView.as_view(),name = 'detail'),
    path('add-to-cart/',landing_views.AddItemsToCartView.as_view(),name = 'add_to_cart'),
    path('search/',landing_views.ItemsSearchView.as_view(),name = 'search'),
]