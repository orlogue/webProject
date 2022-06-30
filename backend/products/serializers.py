from rest_framework import serializers

from .models import Product, Category, SubCategory


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name')
    seller = serializers.CharField(source='seller.name')
    building = serializers.CharField(source='seller.building')

    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    # subcategory = serializers.StringRelatedField(many=True, read_only=True)
    # subcategory = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Category
        fields = '__all__'


class SubCategorySerializer(serializers.ModelSerializer):
    # category = CategorySerializer(read_only=True)

    class Meta:
        model = SubCategory
        fields = '__all__'