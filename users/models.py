from django.contrib.auth.models import AbstractUser

from simple_email_confirmation.models import SimpleEmailConfirmationUserMixin
# Create your models here.

class CustomUser(SimpleEmailConfirmationUserMixin, AbstractUser):
    """
    This user model extends the Django `AbstractUser` model,
    with a `__str__()` method added to show the
    user's username. (Basically a fully blown User model, but this is inherited from
    the model `AbstractUser`. I could not use the AbstractUser model directly
    because the model is abstract, which
    would cause an error.)
    """

    def __str__(self) -> str:
        return f"{self.username}"