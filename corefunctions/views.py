from django.views import View
from django.http import JsonResponse
from django.core.mail import send_mail
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import random
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from twilio.rest import Client
from .serializers import *
from .models import *

ACCOUNT_SID = 'ACebfd4972dfb43f69d4d1afae2832e841'
AUTH_TOKEN = '7189e97a17ed91b0c06ba1d95db7b199'
TWILIO_NUMBER = '+13217326189'
client = Client(ACCOUNT_SID, AUTH_TOKEN)

@api_view(['POST'])
@permission_classes([AllowAny])
def send_otp(request):
    data = request.data  # DRF parses JSON data into the .data attribute
    phone_number = data.get('phone_number')
    sentotp = data.get('sentotp')
    if not phone_number:
        return Response({'error': 'Phone number is required'}, status=status.HTTP_400_BAD_REQUEST)

    otp = sentotp
    message = f"Your OTP is {otp}"

    try:
        message_response = client.messages.create(
            body=message,
            from_=TWILIO_NUMBER,
            to=phone_number
        )
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response({'message': 'OTP sent successfully', 'otp': otp}, status=status.HTTP_200_OK)

class CartItemListView(APIView):
    def get(self, request):
        mobile_no = request.query_params.get('mobile_no')
        if not mobile_no:
            return Response({'error': 'Mobile number is required'}, status=status.HTTP_400_BAD_REQUEST)

        cart_items = CartItem.objects.filter(mobile_no=mobile_no)
        serializer = CartItemSerializer(cart_items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        mobile_no = request.data.get('mobile_no')
        if not mobile_no:
            return Response({'error': 'Mobile number is required'}, status=status.HTTP_400_BAD_REQUEST)

        cart_items = CartItem.objects.filter(mobile_no=mobile_no)
        if not cart_items.exists():
            return Response({'error': 'No cart items found for the provided mobile number'}, status=status.HTTP_404_NOT_FOUND)

        serialized_items = []
        for cart_item in cart_items:
            serializer = CartItemSerializer(cart_item, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                serialized_items.append(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(serialized_items)

    def delete(self, request):
        mobile_no = request.data.get('mobile_no')
        if not mobile_no:
            return Response({'error': 'Mobile number is required'}, status=status.HTTP_400_BAD_REQUEST)

        cart_items = CartItem.objects.filter(mobile_no=mobile_no)
        if not cart_items.exists():
            return Response({'error': 'No cart items found for the provided mobile number'}, status=status.HTTP_404_NOT_FOUND)

        cart_items.delete()
        return Response({'message': 'Cart items deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

class CartItemDetailView(APIView):
    def get_object(self, pk):
        try:
            return CartItem.objects.get(pk=pk)
        except CartItem.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        cart_item = self.get_object(pk)
        serializer = CartItemSerializer(cart_item)
        return Response(serializer.data)

    def patch(self, request, pk):
        cart_item = self.get_object(pk)
        serializer = CartItemSerializer(cart_item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        cart_item = self.get_object(pk)
        cart_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetailView(APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def patch(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserProfileView(APIView):
    def get(self, request, format=None):
        phone_number = request.query_params.get('phone_number')
        if phone_number:
            profile = User.objects.filter(phone_number=phone_number).first()
            if profile:
                serializer = UserSerializer(profile)
                return Response(serializer.data)
            return Response({'message': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'error': 'Phone number is required'}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        phone_number = request.data.get('phone_number')
        if not phone_number:
            return Response({'error': 'Phone number is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        profile = User.objects.filter(phone_number=phone_number).first()
        if profile:
            serializer = UserSerializer(profile)
            return Response(serializer.data, status=status.HTTP_200_OK)

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        phone_number = request.data.get('phone_number')
        if not phone_number:
            return Response({'error': 'Phone number is required'}, status=status.HTTP_400_BAD_REQUEST)

        profile = User.objects.filter(phone_number=phone_number).first()
        if not profile:
            return Response({'message': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self, request, format=None):
        phone_number = request.data.get('phone_number')
        if not phone_number:
            return Response({'error': 'Phone number is required'}, status=status.HTTP_400_BAD_REQUEST)

        profile = User.objects.filter(phone_number=phone_number).first()
        if not profile:
            return Response({'message': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderListView(APIView):
    def get(self, request):
        phone_number = request.query_params.get('phone_number')
        if not phone_number:
            return Response({'error': 'Phone number is required'}, status=status.HTTP_400_BAD_REQUEST)

        orders = Order.objects.filter(mobile_no=phone_number)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        order_serializer = OrderSerializer(data=request.data)
        if order_serializer.is_valid():
            order_serializer.save()
            return Response(order_serializer.data, status=status.HTTP_201_CREATED)
        return Response(order_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderDetailView(APIView):
    def get_object(self, pk):
        try:
            return Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        order = self.get_object(pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def patch(self, request, pk):
        order = self.get_object(pk)
        serializer = OrderSerializer(order, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        order = self.get_object(pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
class MeasurementListView(APIView):
    def get(self, request):
        measurements = Measurement.objects.all()
        serializer = MeasurementSerializer(measurements, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MeasurementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MeasurementDetailView(APIView):
    def get_object(self, pk):
        try:
            return Measurement.objects.get(pk=pk)
        except Measurement.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        measurement = self.get_object(pk)
        serializer = MeasurementSerializer(measurement)
        return Response(serializer.data)

    def patch(self, request, pk):
        measurement = self.get_object(pk)
        serializer = MeasurementSerializer(measurement, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        measurement = self.get_object(pk)
        measurement.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TaskListView(APIView):
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskDetailView(APIView):
    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        task = self.get_object(pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def patch(self, request, pk):
        task = self.get_object(pk)
        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class LeaveView(APIView):
    def get(self, request):
        phone_number = request.query_params.get('phone_number')
        if not phone_number:
            return Response({"message": "Phone number not provided"}, status=status.HTTP_400_BAD_REQUEST)
        
        user = User.objects.filter(phone_number=phone_number).first()
        if not user:
            return Response({"message": "User not found for phone number: {}".format(phone_number)}, status=status.HTTP_404_NOT_FOUND)
        
        leaves = Leave.objects.filter(user=user)
        total_leave = leaves.count()
        total_half_day = leaves.filter(is_half_day=True).count()
        
        salary_details = Salary.objects.filter(user=user).first()
        actual_salary = salary_details.actual_salary if salary_details else None

        response_data = {
            'leaves': LeaveSerializer(leaves, many=True).data,
            'total_leave': total_leave,
            'total_half_day': total_half_day,
            'total_working_days': 30 - total_leave,  # Assuming a 30-day month
            'actual_salary': actual_salary,
        }
        
        return Response(response_data)

    def post(self, request):
        phone_number = request.data.get('phone_number')
        if not phone_number:
            return Response({"message": "Phone number not provided"}, status=status.HTTP_400_BAD_REQUEST)
        
        user = User.objects.filter(phone_number=phone_number).first()
        if not user:
            return Response({"message": "User not found for phone number: {}".format(phone_number)}, status=status.HTTP_404_NOT_FOUND)
        
        leave_serializer = LeaveSerializer(data=request.data)
        if leave_serializer.is_valid():
            leave_serializer.save(user=user)
            return Response(leave_serializer.data, status=status.HTTP_201_CREATED)
        return Response(leave_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, leave_id=None):
        phone_number = request.data.get('phone_number')
        if not phone_number:
            return Response({"message": "Phone number not provided"}, status=status.HTTP_400_BAD_REQUEST)
        
        user = User.objects.filter(phone_number=phone_number).first()
        if not user:
            return Response({"message": "User not found for phone number: {}".format(phone_number)}, status=status.HTTP_404_NOT_FOUND)
        
        leave = Leave.objects.filter(id=leave_id, user=user).first()
        if not leave:
            return Response({"message": "Leave request not found"}, status=status.HTTP_404_NOT_FOUND)
        
        status = request.data.get('status')
        if status not in [True, False]:
            return Response({"message": "Invalid status"}, status=status.HTTP_400_BAD_REQUEST)
        
        leave.status = status
        leave.save()
        
        return Response({"message": "Leave status updated"}, status=status.HTTP_200_OK)
        
class SalaryView(APIView):
    def post(self, request):
        phone_number = request.data.get('phone_number')
        user = User.objects.filter(phone_number=phone_number).first()
        if not user:
            return Response({"message": "User not found for phone number: {}".format(phone_number)}, status=status.HTTP_404_NOT_FOUND)
        
        salary_serializer = SalarySerializer(data=request.data)
        if salary_serializer.is_valid():
            salary_serializer.save(user=user)
            return Response(salary_serializer.data, status=status.HTTP_201_CREATED)
        return Response(salary_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
# Views for EmployeeDetail model
class EmployeeDetailView(APIView):
    def get(self, request):
        employees = EmployeeDetail.objects.all()
        serializer = EmployeeDetailSerializer(employees, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmployeeDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployeeDetailDetail(APIView):
    def get_object(self, pk):
        try:
            return EmployeeDetail.objects.get(pk=pk)
        except EmployeeDetail.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        employee = self.get_object(pk)
        serializer = EmployeeDetailSerializer(employee)
        return Response(serializer.data)

    def patch(self, request, pk):
        employee = self.get_object(pk)
        serializer = EmployeeDetailSerializer(employee, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        employee = self.get_object(pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Views for ManagerProfile model
class ManagerProfileView(APIView):
    def get(self, request):
        managers = ManagerProfile.objects.all()
        serializer = ManagerProfileSerializer(managers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ManagerProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ManagerProfileDetail(APIView):
    def get_object(self, pk):
        try:
            return ManagerProfile.objects.get(pk=pk)
        except ManagerProfile.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        manager = self.get_object(pk)
        serializer = ManagerProfileSerializer(manager)
        return Response(serializer.data)

    def patch(self, request, pk):
        manager = self.get_object(pk)
        serializer = ManagerProfileSerializer(manager, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        manager = self.get_object(pk)
        manager.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Views for ShiftTask model
class ShiftTaskView(APIView):
    def get(self, request):
        tasks = ShiftTask.objects.all()
        serializer = ShiftTaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ShiftTaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ShiftTaskDetail(APIView):
    def get_object(self, pk):
        try:
            return ShiftTask.objects.get(pk=pk)
        except ShiftTask.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        task = self.get_object(pk)
        serializer = ShiftTaskSerializer(task)
        return Response(serializer.data)

    def patch(self, request, pk):
        task = self.get_object(pk)
        serializer = ShiftTaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Views for Stock model
class StockView(APIView):
    def get(self, request):
        stocks = Stock.objects.all()
        serializer = StockSerializer(stocks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StockSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StockDetail(APIView):
    def get_object(self, pk):
        try:
            return Stock.objects.get(pk=pk)
        except Stock.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        stock = self.get_object(pk)
        serializer = StockSerializer(stock)
        return Response(serializer.data)

    def patch(self, request, pk):
        stock = self.get_object(pk)
        serializer = StockSerializer(stock, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        stock = self.get_object(pk)
        stock.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Views for DeliveryPerson model
class DeliveryPersonView(APIView):
    def get(self, request):
        delivery_persons = DeliveryPerson.objects.all()
        serializer = DeliveryPersonSerializer(delivery_persons, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DeliveryPersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeliveryPersonDetail(APIView):
    def get_object(self, pk):
        try:
            return DeliveryPerson.objects.get(pk=pk)
        except DeliveryPerson.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        delivery_person = self.get_object(pk)
        serializer = DeliveryPersonSerializer(delivery_person)
        return Response(serializer.data)

    def patch(self, request, pk):
        delivery_person = self.get_object(pk)
        serializer = DeliveryPersonSerializer(delivery_person, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        delivery_person = self.get_object(pk)
        delivery_person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Views for DeliveryStatus model
# Views for DeliveryStatus model
class DeliveryStatusView(APIView):
    def get(self, request):
        delivery_statuses = DeliveryStatus.objects.all()
        serializer = DeliveryStatusSerializer(delivery_statuses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DeliveryStatusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeliveryStatusDetail(APIView):
    def get_object(self, pk):
        try:
            return DeliveryStatus.objects.get(pk=pk)
        except DeliveryStatus.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        delivery_status = self.get_object(pk)
        serializer = DeliveryStatusSerializer(delivery_status)
        return Response(serializer.data)

    def patch(self, request, pk):
        delivery_status = self.get_object(pk)
        serializer = DeliveryStatusSerializer(delivery_status, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        delivery_status = self.get_object(pk)
        delivery_status.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class InterviewUploadView(APIView):
    def post(self, request, format=None):
        serializer = InterviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)