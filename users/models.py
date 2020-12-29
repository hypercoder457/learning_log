from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """
    This user model extends the Django `AbstractUser` model,
    with a `__str__()` method added to show the
    user's username. (Basically a fully blown User model, but this is inherited from
    the model `AbstractUser`. I could not use the AbstractUser model directly
    because the model is abstract, which
    would cause an error.)
    """
    email = models.EmailField(
        'Email address',
        unique=True,
        error_messages={'unique': 'A user with that email already exists.'},
        help_text="Required. Emails MUST be UNIQUE."
    )

    def __str__(self) -> str:
        return f"{self.username}"
