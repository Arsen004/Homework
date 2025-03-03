from django.contrib import admin
from django.urls import path
from app.views import add_book

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add-book/', add_book, name='add_book')
]
