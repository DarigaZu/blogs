from django.urls import path
from apps.likes import views

urlpatterns = [
    path('likes/', views.like_list, name='like_list'),
    path('likes/create/blog_id', views.like_create, name='like_create'),
    path('likes/update/<int:pk>/', views.like_update, name='like_update'),
    path('likes/delete/<int:pk>/', views.like_delete, name='like_delete'),
]
