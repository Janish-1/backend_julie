from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.ApiOverview, name='home'),
    path('addimage/', views.add_image, name='addimage'),
    path('getimages/',views.get_image, name='getimage'),
    path('updateimages/<int:pk>/', views.update_image, name='updateimage'),
    path('deleteimages/<int:pk>/',views.delete_image, name='deleteimage'),
]
