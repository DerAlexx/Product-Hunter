from django.conf.urls import url
from django.urls import path,include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('product.urls')),
    path('', include('authSys.urls')),
    path('rest/', include('rest_framework.urls', namespace='rest_framework')),
]
