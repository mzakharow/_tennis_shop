from django.conf.urls import url
from django.urls import path
from ecomapp.views import base_view, product_view, category_view

app_name = 'ecomapp'

urlpatterns = [
    path('category/<category_slug>', category_view, name='category_detail'),
    path(r'', base_view, name='base'),
]