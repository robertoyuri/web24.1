from django.contrib import admin
from django.urls import path
from .views import home, second, createpac, createmed, createcons, readpac, readmed

urlpatterns = [
    path('', home, name='home'),
    path('createpac/', createpac, name='createpac'),
    path('createmed/', createmed, name='createmed'),
    path('createcons/', createcons, name='createcons'),
    path('readpac/', readpac, name='readpac'),
    path('readmed/', readmed, name='readmed'),
    path('second/', second, name='second'),
]
