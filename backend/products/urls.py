from django.urls import path
from .views import *

urlpatterns = [
    path('products/', ProductList.as_view()),
    path('products/create/', ProductCreate.as_view()),
    path('products/mine/', MyProductList.as_view()),
    path('products/<int:pk>', ProductDetailByID.as_view()),
    path('products/<slug:slug>', ProductDetail.as_view()),
    path('products/<slug:slug>/update/', ProductUpdate.as_view()),
    path('category/', CategoryViewSet.as_view({'get': 'list'})),
    path('category/<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve'})),
    path('category/subcategory/', SubCategoryList.as_view()),
]
