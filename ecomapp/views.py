from django.shortcuts import render
from ecomapp.models import Category, Product

def base_view(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categories': categories,
        'products': products
    }
    return render(request, 'ecomapp/index.html', context)