from django.urls import path
from .views import *

urlpatterns = [
    path('send-otp-mobile/', send_otp, name='send-otp-mobile'),
    path('cart-items/', CartItemListView.as_view(), name='cart-item-list'),
    path('cart-items/<int:pk>/', CartItemDetailView.as_view(), name='cart-item-detail'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('user-profile/', UserProfileView.as_view(), name='user_profile'),
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('leave/', LeaveView.as_view(), name='leave'),
    path('salary/', SalaryView.as_view(), name='salary'),
    path('manager/', ManagerProfileView.as_view(), name='manager-profile'),
    path('employee/', EmployeeDetailView.as_view(), name='employee-detail'),
    path('shifttask/', ShiftTaskView.as_view(), name='shift-task'),
    path('stock/', StockView.as_view(), name='stock'),
    path('deliveryperson/', DeliveryPersonView.as_view(), name='delivery-person'),
    path('deliverystatus/', DeliveryStatusView.as_view(), name='delivery-status'),
    path('deliverystatus/<int:pk>/', DeliveryStatusDetail.as_view(), name='deliverystatus-detail'),
    path('api/interviews/', InterviewUploadView.as_view(), name='interview-upload'),
    path('measurements/', MeasurementListView.as_view(), name='measurement_list'),
    path('measurements/<int:pk>/', MeasurementDetailView.as_view(), name='measurement_detail'),
] 
