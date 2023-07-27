from django.contrib import admin
from django.urls import path, include
from .views import domashka

urlpatterns = [
    path('lesson4/', domashka)
]
