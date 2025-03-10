from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, FamousAuthor

def add_data(request):
    author, _ = Author.objects.get_or_create(name="Джордж Оруэлл", email="orwell@example.com", birth_date="1903-06-25")
    
    famous_author, _ = FamousAuthor.objects.get_or_create(
        name="Лев Толстой", email="tolstoy@example.com", birth_date="1828-09-09",
        awards="Нобелевская премия (почетный номинант), Пушкинская премия"
    )

    return HttpResponse("Данные успешно добавлены!")

