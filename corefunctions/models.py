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

class CartItem(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.quantity} x {self.title} in cart"

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('Shirt','Shirt'),
        ('T-Shirt','T-Shirt'),
        ('Pants','Pants')
    ]
    title = models.CharField(max_length=255,null=True)
    description = models.TextField(max_length=255,null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) 
    image = models.ImageField(upload_to='product_images/')
    categories = models.CharField(max_length=255, choices=CATEGORY_CHOICES, null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return self.title
