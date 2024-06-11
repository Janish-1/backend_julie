from django.contrib import admin
from .models import (
    User,
    Order,
    CartItem,
    Product,
    Task,
    Leave,
    Salary,
    DeliveryPerson,
    DeliveryStatus,
    Stock,
    ManagerProfile,
    EmployeeDetail,
    Interview
)

class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone_number', 'name', 'active', 'date_added', 'last_update')
    search_fields = ('email', 'phone_number', 'name')
    list_filter = ('active', 'date_added')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('title', 'mobile_no', 'quantity', 'price', 'discounted_price', 'total_price', 'created_at', 'updated_at')
    search_fields = ('title', 'mobile_no')
    list_filter = ('created_at', 'updated_at')

class CartItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'mobile_no', 'quantity', 'price', 'discounted_price', 'total_price', 'created_at', 'updated_at')
    search_fields = ('title', 'mobile_no')
    list_filter = ('created_at', 'updated_at')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'discounted_price', 'categories', 'created_at', 'updated_at')
    search_fields = ('title', 'categories')
    list_filter = ('created_at', 'updated_at', 'categories')

class TaskAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'status', 'start_date_time', 'site_address', 'site_contact', 'assigned_to')
    search_fields = ('project_name', 'status', 'site_address', 'site_contact')
    list_filter = ('status', 'start_date_time')

class LeaveAdmin(admin.ModelAdmin):
    list_display = ('user', 'start_date', 'end_date', 'is_half_day', 'reason', 'status')
    search_fields = ('user__email', 'reason')
    list_filter = ('status', 'start_date', 'end_date')

class SalaryAdmin(admin.ModelAdmin):
    list_display = ('user', 'month', 'base_salary', 'leaves_taken', 'actual_salary')
    search_fields = ('user__email', 'month')
    list_filter = ('month',)

class DeliveryPersonAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__email',)

class DeliveryStatusAdmin(admin.ModelAdmin):
    list_display = ('order', 'status', 'timestamp')
    search_fields = ('order__title', 'status')
    list_filter = ('timestamp',)

class StockAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'last_restocked')
    search_fields = ('product__title',)
    list_filter = ('last_restocked',)

class ManagerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'department', 'team_size')
    search_fields = ('user__email', 'department')

class EmployeeDetailAdmin(admin.ModelAdmin):
    list_display = ('user', 'manager', 'department', 'designation', 'hire_date')
    search_fields = ('user__email', 'manager__email', 'department', 'designation')
    list_filter = ('hire_date',)

class InterviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'video_url', 'uploaded_at')
    search_fields = ('title', 'video_url')
    list_filter = ('uploaded_at',)

admin.site.register(User, UserAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(CartItem, CartItemAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Leave, LeaveAdmin)
admin.site.register(Salary, SalaryAdmin)
admin.site.register(DeliveryPerson, DeliveryPersonAdmin)
admin.site.register(DeliveryStatus, DeliveryStatusAdmin)
admin.site.register(Stock, StockAdmin)
admin.site.register(ManagerProfile, ManagerProfileAdmin)
admin.site.register(EmployeeDetail, EmployeeDetailAdmin)
admin.site.register(Interview, InterviewAdmin)
