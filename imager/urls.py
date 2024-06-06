from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.ApiOverview, name='home'),
    # Image Routes
    path('addimage/', views.add_image, name='addimage'),
    path('getimages/',views.get_image, name='getimage'),
    path('updateimages/<int:pk>/', views.update_image, name='updateimage'),
    path('deleteimages/<int:pk>/',views.delete_image, name='deleteimage'),
    # Files Routes
    path('addfile/', views.add_file, name='addfile'),
    path('getfiles/',views.get_file, name='getfiles'),
    path('updatefiles/<int:pk>/', views.update_file, name='updatefiles'),
    path('deletefiles/<int:pk>/',views.delete_file, name='deletefiles'),
    # Model Render
    path('modelrender/',views.modelrender,name='modelrender'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
