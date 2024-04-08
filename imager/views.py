from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers,status
from django.shortcuts import get_object_or_404
from .models import Image,d3Model
from .serializers import ImageSerializer,d3ModelSerializer
 
@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        '(POST)Add Image': 'api/addimage/',
        '(GET)Get All Images': 'api/getimages/',
        '(GET)Get Single Image':'api/getimages/?name=<str:name>',
        '(PATCH)Update Image Field':'api/updateimages/<int:id>/',
        '(DELETE)Delete Image':'api/deleteimages/<int:id>/',
        '(POST)Add File': 'api/addfile/',
        '(GET)Get All Files': 'api/getfiles/',
        '(GET)Get Single File':'api/getfiles/?name=<str:name>',
        '(PATCH)Update File':'api/updatefiles/<int:id>/',
        '(DELETE)Delete File':'api/deletefiles/<int:id>/',

    }
 
    return Response(api_urls)

@api_view(['POST'])
def add_image(request):
    image = ImageSerializer(data=request.data)
 
    # validating for already existing data
    if Image.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
 
    if image.is_valid():
        image.save()
        return Response(image.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_image(request):
    # checking for the parameters from the URL
    if request.query_params:
        image = Image.objects.filter(**request.query_params.dict())
    else:
        image = Image.objects.all()
 
    # if there is something in items else raise error
    if image:
        serializer = ImageSerializer(image, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['PATCH'])
def update_image(request, pk):
    try:
        image = Image.objects.get(pk=pk)
    except Image.DoesNotExist:
        return Response({'error': 'Image not found'}, status=status.HTTP_404_NOT_FOUND)
    
    # Get the old URL of the image
    old_url = image.url
    
    serializer = ImageSerializer(instance=image, data=request.data, partial=True)
    if serializer.is_valid():
        # Check if there's a new URL being provided in the request
        new_url = request.data.get('url')
        if new_url and new_url != old_url:
            # Delete the old image associated with the old URL
            old_image = Image.objects.filter(url=old_url)
            if old_image.exists():
                old_image.delete()
        
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
def delete_image(request, pk):
    image = get_object_or_404(Image, pk=pk)
    try:
        image.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    except:
        return Response({'error': 'Failed to delete image'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def add_file(request):
    image = d3ModelSerializer(data=request.data)
 
    # validating for already existing data
    if d3Model.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
 
    if image.is_valid():
        image.save()
        return Response(image.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_file(request):
    # checking for the parameters from the URL
    if request.query_params:
        image = d3Model.objects.filter(**request.query_params.dict())
    else:
        image = d3Model.objects.all()
 
    # if there is something in items else raise error
    if image:
        serializer = d3ModelSerializer(image, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['PATCH'])
def update_file(request, pk):
    try:
        image = d3Model.objects.get(pk=pk)
    except d3Model.DoesNotExist:
        return Response({'error': 'Image not found'}, status=status.HTTP_404_NOT_FOUND)
    
    # Get the old URL of the image
    old_url = image.url
    
    serializer = d3ModelSerializer(instance=image, data=request.data, partial=True)
    if serializer.is_valid():
        # Check if there's a new URL being provided in the request
        new_url = request.data.get('url')
        if new_url and new_url != old_url:
            # Delete the old image associated with the old URL
            old_image = d3Model.objects.filter(url=old_url)
            if old_image.exists():
                old_image.delete()
        
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
def delete_file(request, pk):
    image = get_object_or_404(d3Model, pk=pk)
    try:
        image.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    except:
        return Response({'error': 'Failed to delete image'}, status=status.HTTP_400_BAD_REQUEST)
