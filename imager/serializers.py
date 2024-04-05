
from django.db.models import fields
from rest_framework import serializers
from .models import Item
 
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('name', 'url')
