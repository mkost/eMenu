from django.contrib import admin

from .models import Dish
from .models import Card


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    pass


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    pass
