from django.urls import path
from . import views as landing_views

app_name = 'landing'
urlpatterns = [
    path('',landing_views.ProductListView.as_view(),name = 'home'),
    path('product/<int:pk>/',landing_views.ProductDetailView.as_view(),name = 'detail'),
    path('cart/',landing_views.CartListView.as_view(),name = 'cart'),
    path('add-to-cart/',landing_views.AddItemsToCartView.as_view(),name = 'add_to_cart'),
    path('quantity/change/',landing_views.IncreaseOrDecreaseQuantityView.as_view(),name = 'quantity_change'),
    path('item/delete/',landing_views.DeleteItemFromCartView.as_view(),name = 'delete_item'),
    path('search/',landing_views.ItemsSearchView.as_view(),name = 'search'),
]