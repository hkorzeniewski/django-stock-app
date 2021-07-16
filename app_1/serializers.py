from django.db.models import fields
from rest_framework import serializers
from .models import User
from django.db.models import fields

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ['username', 'email', 'password']
        # read_only_fields = ('username')
