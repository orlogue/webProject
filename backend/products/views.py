from django import template
from django.contrib import messages
from django.shortcuts import render, get_object_or_404

from .models import Category, Product, Order
from cart.forms import CartAddProductForm

from cart.cart import Cart
# from .forms import OrderCreateForm
from .models import OrderItem


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    cart_product_forms = []
    for product in products:
        cart_product_forms.append(CartAddProductForm(quantity_choices=[(i, str(i)) for i in range(1, product.quantity + 1)]))
    return render(request,
                  'profiles/homepage.html',
                  {'category': category,
                   'categories': categories,
                   'products': products,
                   'cart_product_forms': cart_product_forms,})





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


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,)
    cart_product_form = CartAddProductForm(quantity_choices=[(i, str(i)) for i in range(1, product.quantity + 1)])
    return render(request, 'products/detail.html', {'product': product,
                                                    'cart_product_form': cart_product_form})


def order_create(request):
    cart = Cart(request)
    if request.user.is_anonymous:
        messages.error(request, 'Вам сначала необходимо зарегистрироваться!')
        return render(request, 'cart/detail.html', {'cart': cart})
    if request.method == 'POST':
        order = Order.objects.create(buyer=request.user)
        for item in cart:
            OrderItem.objects.create(order=order, product=item['product'],
                                     price=item['price'],
                                     quantity=item['quantity'])
        cart.clear()
        return render(request, 'products/created.html')
    # else:
    #     form = OrderCreateForm()
    return render(request, 'cart/detail.html', {'cart': cart})
