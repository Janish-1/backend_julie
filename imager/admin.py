from django.contrib import admin
from .models import Image,d3Model

# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    fields = ("name","url")

class d3ModelAdmin(admin.ModelAdmin):
    fields=  ("name","url")

admin.site.register(Image, ImageAdmin)
admin.site.register(d3Model, d3ModelAdmin)