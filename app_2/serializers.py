from django.db import models
from rest_framework import serializers
from .models import Company, Prices
from django.db.models import fields

class PricesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prices
        fields = ['date', 'opening_price', 'highest_price', 'lowest_price', 'closing_price']

class CompanySerializer(serializers.ModelSerializer):
    prices = PricesSerializer(many=True)
    class Meta:
        model = Company
        fields = ['id', 'company_name', 'prices']