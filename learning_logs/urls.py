"""Defines URL patterns for `learning_logs`"""

from typing import List

from django.urls import URLPattern, path

from . import views

app_name: str = 'learning_logs'
urlpatterns: List[URLPattern] = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all topics
    path('topics/', views.topics, name='topics'),
    # Detail page for a single topic
    path('topics/<int:topic_id>/', views.single_topic, name='topic'),
    # Page to add a new topic with a FORM
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page for editing a topic.
    path('edit_topic/<int:topic_id>/', views.edit_topic, name='edit_topic'),
    # Page for deleting a topic.
    path('delete_topic/<pk>/', views.TopicDeleteView.as_view(), name='delete_topic'),
    # Page for adding a new entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Page for editing a current entry.
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]
