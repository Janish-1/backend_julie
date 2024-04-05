from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Image
from .serializers import ImageSerializer
 
@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'Get All Images': '/getallimages',
        'Get Single Image': '/images/<str:name>',
    }
 
    return Response(api_urls)
