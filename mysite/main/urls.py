from django.urls import path
from .views import index, book_detail, new_books, random_books, get_post_by_category

urlpatterns = [
    path('', index, name='main'),
    path('<str:name>', index, name='search'),
    path('book_detail/<int:id>/', book_detail, name='book_detail'),
    path('random_list/', random_books, name='random_books'),
    path('new/', new_books, name='new_books'),
    path('genre_detail/<int:id>/', get_post_by_category, name='genre_detail'),
]