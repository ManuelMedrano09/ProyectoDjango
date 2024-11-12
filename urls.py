from django.urls import path
from . import views

urlpatterns = [
    path('', views.primero, name='primero'), 
]
