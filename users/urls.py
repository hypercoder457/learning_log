"""Defines URL patterns for `users` app."""
from typing import List
from django.urls import path, include
from django.urls.resolvers import URLPattern, URLResolver

from . import views

app_name: str = 'users'
urlpatterns: List[URLResolver or URLPattern] = [
    # Include default django authentication URLs.
    path('', include('django.contrib.auth.urls')),
    # Registration page.
    path('register/', views.register, name = 'register'),
]
