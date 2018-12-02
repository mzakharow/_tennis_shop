from django.conf.urls import url
from django.urls import path
from ecomapp.views import base_view

app_name = 'ecomapp'

urlpatterns = [
    path(r'', base_view, name='base'),
]