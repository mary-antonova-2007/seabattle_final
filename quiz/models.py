from django.contrib.auth.models import User
from django.db import models
from django.db.models import ForeignKey, OneToOneField, IntegerField, CASCADE
from store.models import Product


# Create your models here.
class BattleField(models.Model):
    user = OneToOneField(User)
    horizontal_size = IntegerField(default=10)
    vertical_size = IntegerField(default=10)


class Ship(models.Model):
    battlefield = ForeignKey(BattleField, on_delete=CASCADE)
    prize = ForeignKey(Product, on_delete=CASCADE)
    horizontal_index = IntegerField(blank=False)
    vertical_index = IntegerField(blank=False)


class Gift(models.Model):
    product = ForeignKey(Product, on_delete=CASCADE)
    user = ForeignKey(User, on_delete=CASCADE, null=True)
