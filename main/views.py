import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "products.settings")
django.setup()


from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from main.serializers import ReviewSerializer, ProductListSerializer, ProductDetailsSerializer , ReviewsSerializer

from main.models import Product,Review

@api_view(['GET'])
def products_list_view(request):
    products = Product.objects.all()
    data = ProductListSerializer(products,many=True)
    return Response(data.data)


class ProductDetailsView(APIView):
    def get(self, request, product_id):
        products = Product.objects.filter(id = product_id).get()
        reviews = Review.objects.filter(id = product_id).get()
        data = ProductDetailsSerializer(products)
        data2 = ReviewsSerializer(reviews)
        return Response(data.data,data2.data)



# доп задание:
class ProductFilteredReviews(APIView):
    def get(self, request, product_id):
        """обработайте значение параметра mark и
        реализуйте получение отзывов по конкретному товару с определённой оценкой
        реализуйте сериализацию полученных данных
        отдайте отсериализованные данные в Response"""
        pass

x = Review.objects.filter(id = 1).get()
print(x.text)