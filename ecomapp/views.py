from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from ecomapp.models import Category, Product, Cart, CartItem
from django.urls import reverse


def base_view(request):
    categories = Category.objects.all()
    products = Product.objects.all().filter(available=True)
    # cart = Cart.objects.first()
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.item.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id=cart_id)
    context = {
        'categories': categories,
        'products': products,
        'cart': cart
    }
    return render(request, 'ecomapp/index.html', context)


def product_view(request, product_slug):
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.item.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id=cart_id)
    product = Product.objects.get(slug=product_slug)
    context = {
        'product': product
    }
    return render(request, 'ecomapp/product.html', context)


def category_view(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    # products = Product.objects.filter(category=category)
    products = category.product_set.all()  # product_set переменная обратного класса в django
    context = {
        'category': category,
        'products': products
    }
    return render(request, 'ecomapp/category.html', context)


def cart_view(request):
    # cart = Cart.objects.first()
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.item.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id=cart_id)
    context = {
        'cart': cart
    }
    return render(request, 'ecomapp/cart.html', context)


def add_to_cart_view(request, product_slug):
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.item.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id=cart_id)
    product = Product.objects.get(slug=product_slug)
    cart.add_to_cart(product.slug)
    return HttpResponseRedirect(reverse('ecomapp:cart'))


def remove_from_cart_view(request, product_slug):
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.item.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id=cart_id)
    product = Product.objects.get(slug=product_slug)
    cart.remove_from_cart(product.slug)
    return HttpResponseRedirect(reverse('ecomapp:cart'))


# def add_to_cart_view(request, product_slug):
#     try:
#         cart_id = request.session['cart_id']
#         cart = Cart.objects.get(id=cart_id)
#         request.session['total'] = cart.item.count()
#     except:
#         cart = Cart()
#         cart.save()
#         cart_id = cart.id
#         request.session['cart_id'] = cart_id
#         cart = Cart.objects.get(id=cart_id)
#     product = Product.objects.get(slug=product_slug)
#     new_item, _ = CartItem.objects.get_or_create(product=product, item_total=product.price)
#     # cart = Cart.objects.first()
#     # for test_item in cart.item.all():
#     #     test_item
#     if new_item not in cart.item.all():
#         cart.item.add(new_item)
#         cart.save()
#         return HttpResponseRedirect('/cart/')
#         # return HttpResponseRedirect('/ecomapp/cart/')
#     # else:
#         # return HttpResponseRedirect('/cart/')
#     return HttpResponseRedirect('/cart/')
#     # HttpResponse(u'Опаньки')


# def remove_from_cart_view(request, product_slug):
#     try:
#         cart_id = request.session['cart_id']
#         cart = Cart.objects.get(id=cart_id)
#         request.session['total'] = cart.item.count()
#     except:
#         cart = Cart()
#         cart.save()
#         cart_id = cart.id
#         request.session['cart_id'] = cart_id
#         cart = Cart.objects.get(id=cart_id)
#     product = Product.objects.get(slug=product_slug)
#     # for cart_item in cart.item.all():
#     #     if cart_item.product == product:
#     #         cart.item.remove(cart_item)
#     #         cart.save()
#     #         return HttpResponseRedirect('/cart/')
#
#     return HttpResponseRedirect('/cart/')

