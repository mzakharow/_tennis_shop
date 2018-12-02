from django.contrib import admin
from django.urls import path, include

import ecomapp.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    # include(r'^', include('ecomapp.urls')),
    path('', include(ecomapp.urls, namespace='ecomapp')),
]
