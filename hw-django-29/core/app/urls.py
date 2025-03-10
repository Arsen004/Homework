from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('add-data/', add_data, name='add_data'),
    path('books/', book_list, name='book_list')
]
