from django.db import models
import datetime
# Create your models here.


class Prices(models.Model):
    opening_price = models.FloatField()
    highest_price = models.FloatField()
    lowest_price = models.FloatField()
    closing_price = models.FloatField()
    date = models.DateField()


class Company(models.Model):
    COMPANY_NAMES = (
        ('ACP', 'ASSECO'),
        ('ALE', 'ALLEGRO'),
        ('PZU', 'PZU')
    )
    company_name = models.CharField(max_length=10, choices=COMPANY_NAMES)
    prices = models.ManyToManyField(Prices, blank=True)