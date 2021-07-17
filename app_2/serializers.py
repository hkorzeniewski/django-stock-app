from django.db import models
from rest_framework import serializers
from .models import Company, User
from django.db.models import fields


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'company_name', 'date', 'opening_price', 'highest_price', 'lowest_price', 'closing_price']