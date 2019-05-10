from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts, name='post'),
    path('create/', views.createPost, name='createPost'),
    path('<int:post_id>', views.detail, name='detail'),
] 
