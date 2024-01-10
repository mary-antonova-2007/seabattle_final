from django.contrib.auth.models import User
from django.db import models
from django.db.models import OneToOneField, CASCADE, IntegerField


# Create your models here.
class Profile(models.Model):
    user = OneToOneField(User, on_delete=CASCADE)
    shoots = IntegerField(default=0)
