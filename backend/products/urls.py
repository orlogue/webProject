from django.urls import path
from .views import *

urlpatterns = [
    # path('product_list/', product_list, name='product_list'),
    # path('<slug:category_slug>/', product_list, name='product_list_by_category'),
    # path('products/<int:id>/<slug:slug>', product_detail, name='product_detail'),
    # path('orders/create_order', order_create, name='order_create'),
    # path('latest-products/', LatestProductsList.as_view({'get': 'list'})),
    # path('products/<slug:category_slug>/<slug:product_slug>/', ProductDetail.as_view()),
    # path('products/<slug:category_slug>/<slug:product_slug>/', ProductDetail.as_view()),
    path('products/', ProductList.as_view()),
    path('products/create', ProductCreate.as_view()),
    path('products/<slug:slug>', ProductDetail.as_view()),
    path('category/', CategoryViewSet.as_view({'get': 'list'})),
    path('category/<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve'})),
    # path('category/<int:pk>/subcategory/', SubCategoryViewSet.as_view({'get': 'list'})),
    path('category/subcategory/', SubCategoryList.as_view()),

    # path('category/', SubCategoryViewSet.as_view()),

]
