from django.urls import path
from . import views

urlpatterns = [
    path('', views.authors_post, name='author_wall'),
    path('search/', views.user_search, name='user_search'),
]
