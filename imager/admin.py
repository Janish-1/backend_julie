from django.contrib import admin
from .models import Image

# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    fields = ("name","url")

admin.site.register(Image, ImageAdmin)