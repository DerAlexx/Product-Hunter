from . import views
from django.urls import path,include

urlpatterns = [
    path('login', views.login_, name="login"),
    path('logout', views.logout_, name="logout"),
    path('signup', views.sign_up_, name="signUp"),
    path('signin', views.sign_up_, name="signin"),
]
