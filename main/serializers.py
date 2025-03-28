from rest_framework import serializers
from main.models import Product,Review


class ReviewSerializer(serializers.ModelSerializer):
    # реализуйте все поля
    pass


class ProductListSerializer(serializers.Serializer):
    title = serializers.CharField()
    price = serializers.DecimalField(max_digits=10,decimal_places=2)


class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['text']

class ProductDetailsSerializer(serializers.ModelSerializer):
    reviews = ReviewsSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ['title','description','price','reviews']



