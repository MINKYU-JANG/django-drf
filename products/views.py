from django.core.cache import cache
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer


@api_view(['GET'])
def product_list(request):
    cache_key = 'product_list'

    if not cache.get(cache_key):
        print('cache miss')
        products = Product.objects.all()
        serializers = ProductSerializer(products, many=True)
        json_response = serializers.data
        cache.set(cache_key, json_response, 50)

    response_date = cache.get(cache_key)
    return Response(response_date)
