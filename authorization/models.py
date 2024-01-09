from django.contrib.auth.models import User
from django.db import models
from django.db.models import OneToOneField, CASCADE


# Create your models here.
class Profile(models.Model):
    user = OneToOneField(User, on_delete=CASCADE)
