from django.contrib import admin
from .models import BattleField, Ship

models = [BattleField, Ship]
# Register your models here.
for model in models:
    admin.site.register(model)
