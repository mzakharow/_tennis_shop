from django.conf.urls import url
from django.urls import path
from shop.views import (base_view,
                        product_view,
                        category_view,
                        cart_view,
                        add_to_cart_view,
                        remove_from_cart_view,
                        change_item_qty,
                        checkout_view,
                        order_create_view,
                        contact_view)

app_name = 'shop'

urlpatterns = [
    path('category/<slug:category_slug>', category_view, name='category_detail'),
    path('product/<slug:product_slug>', product_view, name='product_detail'),
    path('add_to_cart/<slug:product_slug>', add_to_cart_view, name='add_to_cart'),
    path('remove_from_cart/<slug:product_slug>', remove_from_cart_view, name='remove_from_cart'),
    path('change_item_qty', change_item_qty, name='change_item_qty'),
    path('checkout', checkout_view, name='checkout'),
    path('order/', order_create_view, name='create_order'),
    path('cart', cart_view, name='cart'),
    path('contact', contact_view, name='contact'),
    path(r'', base_view, name='base'),
]