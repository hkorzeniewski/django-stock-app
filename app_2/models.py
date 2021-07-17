from django.db import models
import datetime
# Create your models here.


class Prices(models.Model):
    opening_price = models.DecimalField(max_digits=2, decimal_places=2)
    highest_price = models.DecimalField(max_digits=2, decimal_places=2)
    lowest_price = models.DecimalField(max_digits=2, decimal_places=2)
    closing_price = models.DecimalField(max_digits=2, decimal_places=2)
    date = models.DateField()


class Company(models.Model):
    COMPANY_NAMES = (
        ('ACP', 'ASSECO'),
        ('ALE', 'ALLEGRO'),
        ('CCC', 'CCC')
    )
    company_name = models.CharField(max_length=10, choices=COMPANY_NAMES)
    prices = models.ForeignKey(Prices, on_delete=models.PROTECT)