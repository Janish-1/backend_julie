from django.contrib import admin
from .models import CartItem,Product,Order

class cartAdmin(admin.ModelAdmin):
    fields = ('title','quantity','price','discounted_price','total_price')

class productAdmin(admin.ModelAdmin):
    fields = ('title','description','price','categories','discounted_price','image')

admin.site.register(CartItem, cartAdmin)
admin.site.register(Product, productAdmin)
admin.site.register(Order)