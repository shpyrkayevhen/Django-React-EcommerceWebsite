from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Product


class ProductSerialezer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'
