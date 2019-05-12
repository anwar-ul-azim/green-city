from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create, name='createCycle'),
    path('<int:id>', views.cycleView, name='cycleView'),
    path('dropcycle/', views.dropcycle, name='dropcycle'),
    path('pickcycle/', views.pickcycle, name='pickcycle'),
]
