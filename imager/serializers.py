
from django.db.models import fields
from rest_framework import serializers
from .models import Image
 
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('name', 'url','created_at','updated_at')
