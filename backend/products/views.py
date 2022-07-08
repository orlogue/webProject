from django.db.models import Q
from rest_framework import generics, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from .serializers import *
from .models import Product, Category, SubCategory


class LatestProductsList(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.order_by('-created')
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class ProductListPagination(PageNumberPagination):
    page_size = 10


class ProductList(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
    pagination_class = ProductListPagination

    def get_queryset(self):
        if self.request.query_params.__len__() == 0:
            return Product.objects.all()

        products = Product.objects.filter(quantity__gt=0)
        building = self.request.query_params.get('building', None)
        category = self.request.query_params.get('category', None)
        sort = self.request.query_params.get('sort', 'newFirst')
        dic = {'newFirst': '-created',
               'oldFirst': 'created',
               'cheapFirst': 'price',
               'expensiveFirst': '-price'}
        if building == 'all' and category == '0':
            return products.exclude(seller__pk=self.request.user.pk).order_by(dic[sort])
        elif building == 'all':
            return products.filter(category__pk=category) \
                .exclude(seller__pk=self.request.user.pk) \
                .order_by(dic[sort])
        elif category == '0':
            return products.filter(seller__building=building) \
                .exclude(seller__pk=self.request.user.pk) \
                .order_by(dic[sort])
        return products \
            .filter(Q(seller__building=building) & Q(category__pk=category)) \
            .exclude(seller__pk=self.request.user.pk) \
            .order_by(dic[sort])


class MyProductList(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(seller__pk=self.request.user.pk).order_by('-created')


class ProductDetailByID(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]


class ProductDetail(generics.RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'


class ProductUpdate(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer
    lookup_field = 'slug'


class ProductCreate(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.order_by('slug')
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class SubCategoryList(generics.ListAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    permission_classes = [IsAuthenticated]
