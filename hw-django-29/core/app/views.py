from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Book

def add_data(request):
    author1, _ = Author.objects.get_or_create(name="Джордж Оруэлл", birth_date="1903-06-25")
    author2, _ = Author.objects.get_or_create(name="Федор Достоевский", birth_date="1821-11-11")

    book1, _ = Book.objects.get_or_create(title="1984", published_year=1949)
    book2, _ = Book.objects.get_or_create(title="Преступление и наказание", published_year=1866)

    book1.authors.add(author1)
    book2.authors.add(author2)

    return HttpResponse("Данные успешно добавлены!")

def book_list(request):
    books = Book.objects.values("title", "authors__name")
    return render(request, "books.html", {"books": books})
