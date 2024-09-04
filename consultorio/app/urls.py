from django.contrib import admin
from django.urls import path
from .views import home, second

urlpatterns = [
    path('', home, name='home'),
    path('second/', second, name='second'),
]
