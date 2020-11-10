from django.db import models
from django.db.models.fields import CharField, DateTimeField, TextField
from django.db.models.fields.related import ForeignKey
from users.models import CustomUser


class Topic(models.Model):
    """A Topic the user is learning about."""
    text: CharField = models.CharField(max_length = 200)
    date_added: DateTimeField = models.DateTimeField(auto_now_add = True)
    owner: ForeignKey = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self) -> str:
        """
        Return a string representation of the model.\n
        Django calls the `__str__()` method to display representations.\n
        NOTE, this is different from many python classes `__repr__()` methods.
        """
        return self.text

class Entry(models.Model):
    """Something specific learned about a topic"""
    topic: ForeignKey = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text: TextField = models.TextField()
    date_added: DateTimeField = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Metadata for the class `Entry`. We set `verbose_name_plural` to entries because if we didn't do this,
        django would treat multiple entries as `Entrys` instead of `Entries`.
        """
        verbose_name_plural: str = 'entries'

    def __str__(self) -> str:
        """Return a string representation of a model"""
        if len(self.text) > 50:
            return f"{self.text[:50]}..."
        else:
            return f"{self.text}"