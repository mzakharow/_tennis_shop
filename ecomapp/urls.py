from django.conf.urls import url
from django.urls import path
from ecomapp.views import base_view, product_view, category_view

app_name = 'ecomapp'

urlpatterns = [
    path('category/<slug:category_slug>', category_view, name='category_detail'),
    path('product/<slug:product_slug>', product_view, name='product_detail'),
    path(r'', base_view, name='base'),
]