from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    """
    This user model extends the Django `AbstractUser` model,
    with some attributes added, and a `__str__()` method added to show the
    user's username. (Basically a fully blown User model, but this is inherited.)
    """
    is_confirmed = False

    def __str__(self) -> str:
        return f"{self.username}"