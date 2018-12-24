from django.conf.urls import url
from . import views
from django.urls import path,include

urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name="createProduct"),
    path('<int:product_id>', views.detail_product, name="details"),
]
