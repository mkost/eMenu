from django.test import TestCase
from django.test import Client
from django.urls import reverse

from .models import Card, Dish


class CardTestCase(TestCase):
    def setUp(self):
        Card.objects.create(name=u'Test CardMenu', description=u'This is a test description')
        Card.objects.create(name=u'New one', description=u'Second test description')
        Dish.objects.create(name=u'Hamburger', description=u'With salt', price=3.5, preparation_time=4,
                            is_vegetarian=False)

    def test_creating_cards(self):
        cards = Card.objects.all()
        self.assertEqual(cards.count(), 2)

    def test_creating_dishes(self):
        dishes = Dish.objects.filter(name=u'Hamburger')
        self.assertEqual(dishes.count(), 1)

    def test_card_display_all(self):
        pass

    def test_card_display_not_empty(self):
        pass

    def test_index_response(self):
        client = Client()
        response = client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
