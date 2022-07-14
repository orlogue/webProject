from rest_framework import serializers

from .models import Product, Category


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name')
    seller = serializers.CharField(source='seller.name')
    seller_id = serializers.PrimaryKeyRelatedField(source='seller', read_only=True)
    building = serializers.CharField(source='seller.building')

    class Meta:
        model = Product
        fields = '__all__'


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'image', 'quantity', 'price', 'seller', 'slug']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
