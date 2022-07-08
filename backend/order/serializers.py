from rest_framework import serializers
from .models import Order, OrderItem
from products.serializers import ProductSerializer


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'quantity', 'product']


class OrderItemSerializerForOrdersList(serializers.ModelSerializer):
    product = ProductSerializer(many=False, read_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'quantity', 'product']


class MyOrdersSerializer(serializers.ModelSerializer):
    items = OrderItemSerializerForOrdersList(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'buyer', 'created', 'updated', 'status', 'items']
# class OrderItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = OrderItem
#         fields = '__all__'
