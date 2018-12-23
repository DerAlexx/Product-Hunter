from django.conf.urls import url
from . import views
from django.urls import path,include

urlpatterns = [
    path('', views.index, name="index"),
]
