from django.urls import path
from . import views

urlpatterns = [
    path('balance/', views.balance, name='balance'),
    path('transition/', views.transition, name='transition'),
    path('cash/', views.cash, name='cash'),
] 
