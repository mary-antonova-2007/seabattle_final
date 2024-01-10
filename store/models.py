from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE, CharField, ImageField, TextField, OneToOneField, DecimalField, ForeignKey, IntegerField, BooleanField


# Create your models here.
class Product(models.Model):
    name = CharField(max_length=128)
    description = TextField()
    price = DecimalField(decimal_places=2, max_digits=10)
    image = ImageField(upload_to='products_images/', blank=True)


class ShopCart(models.Model):
    user = OneToOneField(User, on_delete=CASCADE)


class Order(models.Model):
    user = ForeignKey(User, on_delete=CASCADE)
    phone = CharField(max_length=32)
    address = CharField(max_length=256)
    information = TextField(blank=True)


class ShopCartItem(models.Model):
    shop_cart = ForeignKey(ShopCart, on_delete=CASCADE)
    product = ForeignKey(Product, on_delete=CASCADE)
    quantity = IntegerField(default=1)
    is_paid = BooleanField(default=False)
    order = ForeignKey(Order, on_delete=CASCADE, blank=True, null=True)

    def total_price(self):
        return self.product.price * self.quantity
