from django.db.models import Count
from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework import filters
from rest_framework import viewsets

from .serializers import CardSerializer, CardThinSerializer
from .models import Card, Dish


class IndexView(View):
    template_name = 'index.html'
    items_per_page = 3

    def get(self, request):
        cards = Card.objects.filter(dishes__gt=0).annotate(dishes_count=Count('dishes'))

        page = request.GET.get('page')
        sort_by = request.GET.get('sort_by')
        if sort_by:
            cards = cards.order_by(sort_by)

        paginator = Paginator(cards, self.items_per_page)

        try:
            cards = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            cards = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            cards = paginator.page(paginator.num_pages)
        return render(request, self.template_name, {'cards': cards})


class DetailsView(View):
    template_name = 'details.html'

    def get(self, request, card_pk):
        card = Card.objects.get(id=card_pk)
        dishes = Dish.objects.filter(card=card)
        return render(request, self.template_name, {'card': card, 'dishes': dishes})


class CardViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Card.objects.filter(dishes__gt=0).annotate(dishes_count=Count('dishes'))
    serializer_class = CardSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('name', 'dishes_count')

    def get_serializer_class(self):
        if self.action == 'list':
            return CardThinSerializer
        if self.action == 'retrieve':
            return CardSerializer
        return CardSerializer
