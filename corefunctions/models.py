from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField(unique=True,null=True)
    mobileno = models.CharField(max_length=15,null=True,blank=True)
    address = models.TextField(null=True,blank=True)
    password = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='user_photos/', blank=True, null=True)
    last_update = models.DateTimeField(auto_now=True)
    date_added = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    otp = models.CharField(max_length=10,null=True, blank=True)

    def __str__(self):
        return self.username
