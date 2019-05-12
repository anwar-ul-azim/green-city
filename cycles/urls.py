from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create, name='createCycle'),
    path('<int:id>', views.cycleView, name='cycleView'),
    path('dropcycle/<int:id>', views.dropcycle, name='dropcycle'),
    path('pickcycle/<int:id>', views.pickcycle, name='pickcycle'),
]
