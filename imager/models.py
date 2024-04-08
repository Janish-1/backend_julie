from django.db import models

class Image(models.Model):
    name = models.CharField(max_length=255)
    url = models.ImageField(upload_to='mainfiles/')  # Relative path from MEDIA_ROOT
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class d3Model(models.Model):
    name=models.CharField(max_length=255)
    url = models.FileField(upload_to='3dmodels/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
