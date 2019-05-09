from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create, name='createCycle'),
    path('dropcycle/', views.dropcycle, name='dropcycle'),
    path('pickcycle/', views.pickcycle, name='pickcycle'),
]
