"""Defines URL patterns for `users` app."""
from typing import List, Union

from django.urls import include, path
from django.urls.resolvers import URLPattern, URLResolver

from . import views

app_name: str = 'users'
urlpatterns: List[Union[URLPattern, URLResolver]] = [
    # Include default django authentication URLs.
    path('', include('django.contrib.auth.urls')),
    # Registration page.
    path('register/', views.register, name='register'),
    path('activate/<slug:uidb64>/<slug:token>/',
         views.activate, name='activate')
]
