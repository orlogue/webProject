from django.urls import path
from .views import *

urlpatterns = [
    path('order/', OrderList.as_view()),
    path('order/create/', OrderCreate.as_view()),
    path('order/item/create/', OrderItemCreate.as_view()),
]