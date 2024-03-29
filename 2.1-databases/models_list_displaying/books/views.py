from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from books.models import Book


def index_view(request):
    return redirect('books')

def books_view(request):
    template = 'books/books_list.html'
    query_set = Book.objects.all()
    books = query_set.order_by('pub_date')
    context = {
        'books': books
    }
    return render(request, template, context)

def one_book_view(request, pub_date):
    template = 'books/book.html'
    query_set = Book.objects.all()
    book = query_set.get(pub_date=pub_date)
    CONTENT = query_set.values('pub_date')
    list_date = []
    for one_book in CONTENT:
        list_date.append(one_book['pub_date'])
    list_date_sorted = sorted(list_date)
    previous_page = ''
    next_page = ''
    for n, date_dt in enumerate(list_date_sorted):
        date_str = str(date_dt)
        if pub_date == date_str:
            if pub_date == str(min(list_date_sorted)):
                previous_page = None
            else:
                previous_page = str(list_date_sorted[n - 1])
            if pub_date == str(max(list_date_sorted)):
                next_page = None
            else:
                next_page = str(list_date_sorted[n + 1])
    context = {
        'book': book,
        'previous_page': previous_page,
        'next_page': next_page,
    }
    return render(request, template, context)


# Комментарий преподавателя:

# В дополнительном задании лучше использовать фильтры для создания пагинации книг по дате.
#
# Посмотрите как работать с фильтрами в документации
# https://docs.djangoproject.com/en/4.0/topics/db/queries/#filters-can-reference-fields-on-the-model
#
# Пример
#
# def books_pub_date(request, pub_date):
#     template = 'books/books_list.html'
#     books_objects = Book.objects.filter(pub_date=pub_date)
#     books_next = Book.objects.filter(pub_date__gt=pub_date).order_by('pub_date').first()
#     books_previous = Book.objects.filter(pub_date__lt=pub_date).order_by('-pub_date').first()
#     context = {
#         'books': books_objects,
#         'next_book': books_next,
#         'previous_book': books_previous,
#     }
#     return render(request, template, context)
