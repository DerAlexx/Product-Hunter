from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path,include
from product import views
from authSys import views as authView
from django.contrib import admin

urlpatterns = [
    path('', views.index, name='masterhome'),
    path('product/', include('product.urls')),
    path('', include('authSys.urls')),
    path('rest/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
