from django.urls import path
from . import views

urlpatterns = [
    path('', views.payment, name='payments'),
    path('balance/', views.balance, name='balance'),
    path('cash/', views.cash, name='cash'),
] 
