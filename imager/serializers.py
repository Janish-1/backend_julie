
from django.db.models import fields
from rest_framework import serializers
from .models import Image,d3Model
 
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('name', 'url','created_at','updated_at')


class d3ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('name', 'url','created_at','updated_at')
