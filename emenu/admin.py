from django.contrib import admin

from .models import Dish
from .models import Card


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'preparation_time', 'is_vegetarian')


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
