from django.db.models import Count
from django.test import TestCase
from django.test import Client
from django.urls import reverse

from .models import Card, Dish


class CardTestCase(TestCase):
    def setUp(self):
        pass  # data loaded from fixtures

    def test_filter_dishes(self):
        dishes = Dish.objects.filter(name=u'Hamburger')
        self.assertEqual(dishes.count(), 1)

    def test_card_display_all(self):
        cards = Card.objects.all()
        self.assertEqual(cards.count(), 9)

    def test_card_display_not_empty(self):
        cards = Card.objects.filter(dishes__gt=0).annotate(dishes_count=Count('dishes'))
        self.assertEqual(cards.count(), 8)

    def test_index_response(self):
        client = Client()
        response = client.get(reverse('index') + '?sort_by=name')
        self.assertEqual(response.status_code, 200)

    def test_index_response_empty_page(self):
        client = Client()
        response = client.get(reverse('index') + '?page=100')
        self.assertEqual(response.status_code, 200)

    def test_creating_dish(self):
        dish = Dish.objects.create(name='Test dish', description='Test desc', price=5, preparation_time=3, is_vegetarian=False)
        dish.save()
        last_dish = Dish.objects.all().latest('id')
        self.assertEqual(dish.id, last_dish.id)

    def test_creating_card(self):
        card = Card.objects.create(name='Test card', description='Test description')
        card.save()
        last_card = Card.objects.all().latest('id')
        self.assertEqual(card.id, last_card.id)

    def test_api_response(self):
        client = Client()
        response = client.get(reverse('index_asynchronous'))
        self.assertEqual(response.status_code, 200)

    def test_api_cards_response(self):
        client = Client()
        response = client.get('/api/cards/1/')
        self.assertEqual(response.status_code, 200)

    def test_detail_response(self):
        client = Client()
        response = client.get(reverse('details', args=[2]))
        self.assertEqual(response.status_code, 200)
