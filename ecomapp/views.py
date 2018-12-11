from django.shortcuts import render
from ecomapp.models import Category, Product, Cart, CartItem


def base_view(request):
    categories = Category.objects.all()
    products = Product.objects.all().filter(available=True)
    cart = Cart.objects.first()
    context = {
        'categories': categories,
        'products': products,
        'cart': cart
    }
    return render(request, 'ecomapp/index.html', context)


def product_view(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    context = {
        'product': product
    }
    return render(request, 'ecomapp/product.html', context)


def category_view(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    # products = Product.objects.filter(category=category)
    products = category.product_set.all()   # product_set переменная обратного класса в django
    context = {
        'category': category,
        'products': products
    }
    return render(request, 'ecomapp/category.html', context)

def cart_view(request):
    cart = Cart.objects.first()
    context = {
        'cart': cart
    }
    return render(request, 'ecomapp/cart.html', context)


# def add_to_cart_view(request, product_slug):
#     product = Product.objects.get(slug=product_slug)
#     new_item = CartItem.objects.get_or_create(product=product, item_total=product.price)
#     cart = Cart.objects.first()
#     if new_item not in cart.item.all():
#         cart.item.add(new_item)
#         cart.save()
#         return HttpResponseRedirect('/ecomapp/cart/')
