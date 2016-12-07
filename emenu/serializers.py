from rest_framework import serializers

from .models import Card, Dish


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ('id', 'name', 'description', 'price', 'preparation_time', 'created', 'updated', 'is_vegetarian',
                  'picture')


class CardSerializer(serializers.ModelSerializer):
    dishes = DishSerializer(many=True, read_only=True, required=False, allow_null=True)

    class Meta:
        model = Card
        fields = ('id', 'name', 'dishes')


class CardThinSerializer(serializers.ModelSerializer):
    dishes_count = serializers.IntegerField()

    class Meta:
        model = Card
        fields = ('id', 'name', 'description', 'dishes_count')
