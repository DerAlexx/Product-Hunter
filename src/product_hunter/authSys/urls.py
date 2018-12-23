from . import views
from django.urls import path,include

urlpatterns = [
    path('l', views.index, name="index"),
]
