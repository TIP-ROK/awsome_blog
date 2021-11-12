from django.urls import path
from . import views


urlpatterns = [
    path('<int:pk>/comment_edit/<int:comment_pk>/', views.comment_edit, name='comment_edit'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('<int:pk>/like/', views.like, name='like'),
    path('<int:pk>/like_list/', views.like_list, name='like_list'),
    path('create/', views.post_create, name='post_create'),
    path('<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('', views.post_list, name='post_list'),
    path('search/', views.post_search, name='post_search'),
]
