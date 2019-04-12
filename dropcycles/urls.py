from django.urls import path, include
from . import views

urlpatterns = [
    path('dropcycle', views.dropcycle, name='dropcycle'),
]