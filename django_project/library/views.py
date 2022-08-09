from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from .filters import *

# Create your views here.

def home(request):
    books = Book.objects.all().order_by('title')
    authors = Author.objects.all().order_by('last_name')

    total_authors = authors.count()
    total_books = books.count()
    diverse_authors = authors.filter(non_marginalized=False).count()
    diverse_percentage = round((diverse_authors/total_authors)*100)

    books = books[:15]
    authors = authors[:15]

    context = {'books': books, 'authors': authors, 'total_authors': total_authors,
    'total_books': total_books, 'diverse_percentage': diverse_percentage}

    return render(request, 'library/dashboard.html', context)

def books(request):
    books = Book.objects.all().order_by('title')
    total_number = books.count()

    myFilter = BookFilter(request.GET, queryset=books)
    books = myFilter.qs
    filtered_number = books.count()
    filtered_percent = round((filtered_number/total_number)*100)

    context = {'books': books, 'myFilter': myFilter, 'filtered_percent': filtered_percent,
    'filtered_number': filtered_number, 'total_number': total_number}
    return render(request, 'library/books.html', context)

def authors(request):
    authors = Author.objects.all().order_by('last_name')
    total_number = authors.count()

    myFilter = AuthorFilter(request.GET, queryset=authors)
    authors = myFilter.qs
    filtered_number = authors.count()
    filtered_percent = round((filtered_number/total_number)*100)

    context = {'authors': authors, 'myFilter': myFilter, 'filtered_percent': filtered_percent,
    'filtered_number': filtered_number, 'total_number': total_number}
    return render(request, 'library/authors.html', context)

def author_info(request, pk): # pk stands for primary key, will prob be the id
    author = Author.objects.get(id=pk)
    books = author.books

    myFilter = BookFilter(request.GET, queryset=books)
    books = myFilter.qs

    context = {'author': author, 'books': books, 'myFilter': myFilter}
    return render(request, 'library/author_info.html', context)

def book_info(request, pk):
    book = Book.objects.get(id=pk)
    authors = book.author_set.all()
    authors_neat = []
    char_race_conns = CharRaceConn.objects.filter(character_set__book_title=book.title)
    if CharGenderConn.objects.filter(character_set__book_title=book.title):
        char_gender_conns = CharGenderConn.objects.filter(character_set__book_title=book.title)
    else:
        char_gender_conns = ['unknown']
    for author in authors:
        authors_neat.append(author.full_name)
    context = {'book': book, 'authors': authors, 'authors_neat': authors_neat,
    'char_race_conns': char_race_conns, 'char_gender_conns': char_gender_conns}
    return render(request, 'library/book_info.html', context)

# TODO You may consider creating an About/Definitions page to describe the authoritative language used
# in the app and what functionality is available.