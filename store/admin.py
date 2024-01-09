from django.contrib import admin
from .models import Product, ShopCart, ShopCartItem


# Register your models here.
models = [Product, ShopCart, ShopCartItem]
for model in models:
    admin.site.register(model)
