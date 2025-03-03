from django.shortcuts import render, redirect
from .forms import BookForm

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')  # успешная отправка
        else:
            return render(request, 'add_book.html', {'form': form})  # не успешная отправка

    form = BookForm()
    return render(request, 'add_book.html', {'form': form})
