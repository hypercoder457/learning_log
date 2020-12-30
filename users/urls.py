"""Defines URL patterns for `users` app."""
from typing import List, Union

from django.contrib.auth import views as auth_views
from django.urls import include, path, reverse_lazy
from django.urls.resolvers import URLPattern, URLResolver

from . import views

app_name: str = 'users'
urlpatterns: List[Union[URLPattern, URLResolver]] = [
    # Include default django authentication URLs.
    path('', include('django.contrib.auth.urls')),
    # Registration page.
    path('register/', views.register, name='register'),
    path('activate/<slug:uidb64>/<slug:token>/',
         views.activate, name='activate'),
    path('reset_password/', auth_views.PasswordResetView.as_view(
        template_name='registration/password_reset_form.html',
        email_template_name='registration/password_reset_email.html',
        subject_template_name='registration/password_reset_subject.txt',
        success_url=reverse_lazy('users:password_reset_done')
    ), name='reset_password'),
    path('reset_password/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='registration/password_reset_done.html'
    ), name='reset_password_done'),
    path('reset_password/confirm/<slug:uidb64>/<slug:token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='registration/password_reset_confirm.html',
             success_url=reverse_lazy('users:reset_password_complete')
         ), name='reset_password_confirm'),
    path('reset_password/complete/', auth_views.PasswordResetCompleteView.as_view(),
         name='reset_password_complete'),
]
