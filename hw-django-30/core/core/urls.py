from django.contrib import admin
from django.urls import path
from app.views import add_data

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add-data/', add_data, name='add_data')
]
