from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six


class MyTokenGenerator(PasswordResetTokenGenerator):
    """
    A confirmation token generator,
    also for a password reset.
    """

    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(user.is_active)
        )


account_activation_token = MyTokenGenerator()
