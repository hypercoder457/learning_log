from typing import Dict, List, Type

from django import forms
from django.forms.widgets import Textarea

from .models import Entry, Topic


class TopicForm(forms.ModelForm):
    class Meta:
        model: Type[Topic] = Topic
        fields: List[str] = ['text']
        labels: Dict[str, str] =  {
            'text': '' 
        }
        
class EntryForm(forms.ModelForm):
    class Meta:
        model: Type[Entry] = Entry
        fields: List[str] = ['text']
        labels: Dict[str, str] = {
            'text': ''
        }

        widgets: Dict[str, Textarea] = {
            'text': forms.Textarea(
                attrs = {
                    'cols': 80
                }
            )
        }
