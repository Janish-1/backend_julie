from rest_framework import serializers
from .models import User, Order, CartItem, Product, Task, Leave, Salary, DeliveryPerson, DeliveryStatus, Stock, ManagerProfile, EmployeeDetail, Interview

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class LeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leave
        fields = '__all__'

class SalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Salary
        fields = '__all__'

class DeliveryPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryPerson
        fields = '__all__'

class DeliveryStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryStatus
        fields = '__all__'

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'

class ManagerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManagerProfile
        fields = '__all__'

class EmployeeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeDetail
        fields = '__all__'

class InterviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interview
        fields = ['title', 'video_url']