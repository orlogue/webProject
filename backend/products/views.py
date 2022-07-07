import requests
from django.contrib import messages
from django.db.models import Q
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response

from cart.forms import CartAddProductForm

from cart.cart import Cart
# from .forms import OrderCreateForm
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


class ProductList(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        if self.request.query_params.__len__() == 0:
            return Product.objects.all()
        building = self.request.query_params.get('building', None)
        category = self.request.query_params.get('category', None)
        sort = self.request.query_params.get('sort', 'newFirst')
        dic = {'newFirst': '-created',
               'oldFirst': 'created',
               'cheapFirst': 'price',
               'expensiveFirst': '-price'}
        if building == 'all' and category == '0':
            return Product.objects.exclude(seller__pk=self.request.user.pk).order_by(dic[sort])
        elif building == 'all':
            return Product.objects.filter(category__pk=category) \
                .exclude(seller__pk=self.request.user.pk) \
                .order_by(dic[sort])
        elif category == '0':
            return Product.objects.filter(seller__building=building) \
                .exclude(seller__pk=self.request.user.pk) \
                .order_by(dic[sort])
        return Product.objects \
            .filter(Q(seller__building=building) & Q(category__pk=category)) \
            .exclude(seller__pk=self.request.user.pk) \
            .order_by(dic[sort])


class MyProductList(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(seller__pk=self.request.user.pk).order_by('-created')


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


# class SubCategoryViewSet(viewsets.ReadOnlyModelViewSet):
#     serializer_class = SubCategorySerializer
#
#     def get_queryset(self):
#         category_pk = self.kwargs['pk']
#         return SubCategory.objects.filter(category__pk=category_pk)
#
#     def get_permissions(self):
#         if self.action == 'list' or self.action == 'retrieve':
#             permission_classes = [AllowAny]
#         else:
#             permission_classes = [IsAdminUser]
#         return [permission() for permission in permission_classes]

class SubCategoryList(generics.ListAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    permission_classes = [IsAuthenticated]

    # def get_queryset(self):
    #     category_pk = self.kwargs['pk']
    #     return SubCategory.objects.filter(category__pk=category_pk)


#
# class CategoriesList(APIView):
#     def get(self, request):
#         category = Category.objects.order_by('id')
#         serializer = CategorySerializer(category, many=True)
#         return Response(serializer.data)


# class CategoriesList(generics.API):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    cart_product_forms = []
    for product in products:
        cart_product_forms.append(
            CartAddProductForm(quantity_choices=[(i, str(i)) for i in range(1, product.quantity + 1)]))
    return render(request,
                  'profiles/homepage.html',
                  {'category': category,
                   'categories': categories,
                   'products': products,
                   'cart_product_forms': cart_product_forms, })


#
# register = template.Library()
# @register.simple_tag
# def card_with_current_choices(form, quantity):
#     return form.card_with_current_choices(quantity)
# def product_detail(request, id, slug):
#     product = get_object_or_404(Product,
#                                 id=id,
#                                 slug=slug)
#     return render(request,
#                   'detail.html',
#                   {'product': product})


# def product_detail(request, id, slug):
#     product = get_object_or_404(Product,
#                                 id=id,
#                                 slug=slug, )
#     cart_product_form = CartAddProductForm(quantity_choices=[(i, str(i)) for i in range(1, product.quantity + 1)])
#     return render(request, 'products/detail.html', {'product': product,
#                                                     'cart_product_form': cart_product_form})


# def order_create(request):
#     cart = Cart(request)
#     if request.user.is_anonymous:
#         messages.error(request, 'Вам сначала необходимо зарегистрироваться!')
#         return render(request, 'cart/detail.html', {'cart': cart})
#     if request.method == 'POST':
#         order = Order.objects.create(buyer=request.user)
#         for item in cart:
#             OrderItem.objects.create(order=order, product=item['product'],
#                                      price=item['price'],
#                                      quantity=item['quantity'])
#         cart.clear()
#         return render(request, 'products/created.html')
#     # else:
#     #     form = OrderCreateForm()
#     return render(request, 'cart/detail.html', {'cart': cart})
