from django.db import models

class Image(models.Model):
    name = models.CharField(max_length=255)
    url = models.ImageField('../media/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name