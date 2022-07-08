from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer, MyOrdersSerializer


class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]


class OrderListPagination(PageNumberPagination):
    page_size = 4


class MyOrdersList(generics.ListAPIView):
    serializer_class = MyOrdersSerializer
    pagination_class = OrderListPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(buyer=self.request.user)


class OrderItemList(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]


class MyOrderItemsList(generics.ListAPIView):
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return OrderItem.objects.filter(order__buyer=self.request.user)
