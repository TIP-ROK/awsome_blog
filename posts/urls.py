from django.urls import path
from . import views


urlpatterns = [
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('create/', views.post_create, name='post_create'),
    path('<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('', views.post_list, name='post_list'),
    path('search/', views.post_search, name='post_search'),
]
