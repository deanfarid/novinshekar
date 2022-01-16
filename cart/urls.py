from django.urls import path , include
from . import views

app_name = 'cart'

urlpatterns = [
    path('usercart/', views.OrderSummaryView.as_view(), name="usercart"),
    path('cart/<id>', views.add_to_cart, name="add-to-cart"),
    path('reduce-quantity-item/<id>/', views.reduce_quantity_item, name='reduce-quantity-item'),
    path('remove-from-cart/<id>/', views.remove_from_cart, name='remove-from-cart'),


]