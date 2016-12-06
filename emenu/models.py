# coding=utf-8
from django.db import models
from django.utils import timezone


class Dish(models.Model):
    name = models.CharField(u'nazwa', max_length=255)
    description = models.TextField(u'opis')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    preparation_time = models.IntegerField(help_text=u'w minutach')
    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField(editable=False)
    is_vegetarian = models.BooleanField(default=False)
    picture = models.ImageField(u'zdjęcie', null=True, blank=True, upload_to='dishes/')

    class Meta:
        verbose_name = u'danie'
        verbose_name_plural = u'dania'

    def __unicode__(self):
        return "%s" % (self.name,)

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created = timezone.now()
        self.updated = timezone.now()
        return super(Dish, self).save(*args, **kwargs)


class Card(models.Model):
    name = models.CharField(u'nazwa', max_length=255, unique=True)
    description = models.TextField(u'opis')
    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField(editable=False)
    dishes = models.ManyToManyField(Dish, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = u'karta'
        verbose_name_plural = u'karty'

    def __unicode__(self):
        return "%s" % (self.name,)

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created = timezone.now()
        self.updated = timezone.now()
        return super(Card, self).save(*args, **kwargs)
