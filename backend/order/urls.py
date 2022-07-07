from django.urls import path
from .views import *

urlpatterns = [
    path('order/', Order.as_view()),
    path('order/item/', OrderItem.as_view()),
]