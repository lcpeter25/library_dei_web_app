from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.books, name='books'),
    path('authors/', views.authors, name='authors'),
    path('author_info/<str:pk>/', views.author_info, name='author_info'),
    path('book_info/<str:pk>/', views.book_info, name='book_info'),
]