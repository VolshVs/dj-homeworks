from django.urls import path

from books.views import books_view, one_book_view

urlpatterns = [
    path('', books_view, name='books'),
    path('<slug:pub_date>/', one_book_view, name='pub_date'),
]