from django.urls import path
from .views import *

urlpatterns = [
    path('order/', OrderList.as_view()),
    path('order/mine/', MyOrdersList.as_view()),
    path('order/item/', OrderItemList.as_view()),
]