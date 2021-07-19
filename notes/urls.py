from django.urls import path

from . import views

urlpatterns = [
    path('notes', views.list),
]