from django.conf.urls import url
from django.urls import path,include
from django.contrib import admin
from product import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='masterhome'),
    path('product/', include('product.urls')),
    path('', include('authSys.urls')),
    path('rest/', include('rest_framework.urls', namespace='rest_framework')),
]
