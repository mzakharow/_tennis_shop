from django.conf.urls import url
from django.urls import path
from ecomapp.views import base_view, product_view, category_view, cart_view, add_to_cart_view, remove_from_cart_view

app_name = 'ecomapp'

urlpatterns = [
    path('category/<slug:category_slug>', category_view, name='category_detail'),
    path('product/<slug:product_slug>', product_view, name='product_detail'),
    path('add_to_cart/<slug:product_slug>', add_to_cart_view, name='add_to_cart'),
    path('remove_from_cart/<slug:product_slug>', remove_from_cart_view, name='remove_from_cart'),
    path('cart/', cart_view, name='cart'),
    path(r'', base_view, name='base'),
]