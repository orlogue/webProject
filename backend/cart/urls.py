from django.urls import path
from . import views


urlpatterns = [
    path('cart/detail', views.cart_detail, name='cart_detail'),
    path('cart/cart_detail', views.cart_add, name='cart_add'),
    path('cart_detail', views.cart_remove, name='cart_remove'),
]