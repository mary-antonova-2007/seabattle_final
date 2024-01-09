from django.urls import path
from .views import add_to_cart, shop_cart

urlpatterns = [
    # Другие URL-пути
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('shop_cart/', shop_cart, name='shop_cart'),
    # Возможно, другие URL-пути
]