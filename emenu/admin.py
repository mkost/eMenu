from django.contrib import admin

from .models import Dish
from .models import Card


class DishInline(admin.StackedInline):
    model = Dish


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    inlines = [DishInline,]
