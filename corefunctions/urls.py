from django.urls import path
from .views import sendemail

urlpatterns = [
    path('send_email/', sendemail, name='send_email'),
] 
