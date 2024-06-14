from rest_framework import serializers
from .models import User, Order, CartItem, Product, Task, Leave, Salary, DeliveryPerson, DeliveryStatus, Stock, ManagerProfile, EmployeeDetail, Interview, Measurement

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['id','category', 'chest', 'waist', 'length']

class OrderSerializer(serializers.ModelSerializer):
    measurement = MeasurementSerializer()

    class Meta:
        model = Order
        fields = ['id', 'product', 'title', 'mobile_no', 'quantity', 'price', 'discounted_price', 'total_price', 'measurement', 'style', 'estimate_price', 'color', 'shipping_address', 'created_at', 'updated_at']

    def create(self, validated_data):
        measurement_data = validated_data.pop('measurement')
        measurement = Measurement.objects.create(**measurement_data)
        order = Order.objects.create(measurement=measurement, **validated_data)
        return order

    def update(self, instance, validated_data):
        measurement_data = validated_data.pop('measurement', None)

        if measurement_data:
            measurement = instance.measurement
            for key, value in measurement_data.items():
                setattr(measurement, key, value)
            measurement.save()

        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()

        return instance

class CartItemSerializer(serializers.ModelSerializer):
    measurement = MeasurementSerializer()

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'title', 'mobile_no', 'quantity', 'price', 'discounted_price', 'total_price', 'measurement', 'style', 'estimate_price', 'color', 'shipping_address']

    def create(self, validated_data):
        measurement_data = validated_data.pop('measurement')
        measurement = Measurement.objects.create(**measurement_data)
        cart_item = CartItem.objects.create(measurement=measurement, **validated_data)
        return cart_item

    def update(self, instance, validated_data):
        measurement_data = validated_data.pop('measurement', None)

        if measurement_data:
            measurement = instance.measurement
            for key, value in measurement_data.items():
                setattr(measurement, key, value)
            measurement.save()

        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()

        return instance

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