from django.urls import path
from apps.tags import views

urlpatterns = [
    path('tags/', views.tag_list, name='tag_list'),
    path('tags/create/', views.tag_create, name='tag_create'),
    path('tags/update/<int:pk>/', views.tag_update, name='tag_update'),
    path('tags/delete/<int:pk>/', views.tag_delete, name='tag_delete'),
]
