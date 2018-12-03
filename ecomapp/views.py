from django.shortcuts import render
from ecomapp.models import Category, Product


def base_view(request):
    categories = Category.objects.all()
    products = Product.objects.all().filter(available=True)
    context = {
        'categories': categories,
        'products': products
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
    context = {
        'category': category
    }
    return render(request, 'ecomapp/category.html', context)

