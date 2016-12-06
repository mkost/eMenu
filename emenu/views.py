from django.shortcuts import render
from django.views import View

from .models import Card, Dish


class IndexView(View):
    template_name = 'index.html'

    def get(self, request):
        cards = Card.objects.all()
        return render(request, self.template_name, {'cards': cards})


class DetailsView(View):
    template_name = 'details.html'

    def get(self, request, card_pk):
        card = Card.objects.get(id=card_pk)
        dishes = Dish.objects.filter(card=card)
        return render(request, self.template_name, {'card': card, 'dishes': dishes})
