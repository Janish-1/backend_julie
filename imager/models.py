from django.db import models

class Image(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField()

    def __str__(self) -> str:
        return self.name + self.url