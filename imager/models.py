from django.db import models

class Image(models.Model):
    name = models.CharField(max_length=255)
    url = models.ImageField('../media/')  # Relative path from MEDIA_ROOT
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + self.url
