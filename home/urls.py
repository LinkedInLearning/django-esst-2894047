from django.urls import path

from . import views

urlpatterns = [ 
    path('home', views.home),
    path('authorized', views.authorized),
]