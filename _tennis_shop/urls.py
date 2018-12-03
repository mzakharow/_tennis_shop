from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

import ecomapp.urls
from _tennis_shop import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    # include(r'^', include('ecomapp.urls')),
    path('', include(ecomapp.urls, namespace='ecomapp')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)