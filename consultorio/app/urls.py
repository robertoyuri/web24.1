from django.contrib import admin
from django.urls import path
from .views import home, second, createpac, createmed, createcons, readpac, readmed, updatepac, updatemed, updatecons, deletepac, deletemed, deletecons

urlpatterns = [
    path('', home, name='home'),
    path('createpac/', createpac, name='createpac'),
    path('createmed/', createmed, name='createmed'),
    path('createcons/', createcons, name='createcons'),
    path('readpac/', readpac, name='readpac'),
    path('readmed/', readmed, name='readmed'),
    path('updatepac/<int:id>', updatepac, name='updatepac'),
    path('updatemed/<int:id>', updatemed, name='updatemed'),
    path('updatecons/<int:id>', updatecons, name='updatecons'),
    path('deletepac/<int:id>', deletepac, name='deletepac'),
    path('deletemed/<int:id>', deletemed, name='deletemed'),
    path('deletecons/<int:id>', deletecons, name='deletecons'),
    path('second/', second, name='second'),
]
