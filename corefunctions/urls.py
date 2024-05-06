from django.urls import path
from .views import *

urlpatterns = [
    path('send-otp-mobile/', send_otp, name='send-otp-mobile'),
    path('cart-items/', CartItemListView.as_view(), name='cart-item-list'),
    path('cart-items/<int:pk>/', CartItemDetailView.as_view(), name='cart-item-detail'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('user-profile/', UserProfileView.as_view(), name='user_profile'),
] 
