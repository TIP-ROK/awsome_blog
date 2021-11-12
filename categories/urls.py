from django.urls import path
from . import views


urlpatterns = [
    path('<int:pk>/', views.category_detail, name='category_detail'),
    path('adding/', views.category_adding, name='category_adding'),
    path('<int:pk>/delete/', views.category_delete, name='category_delete'),
]