from typing import Tuple, Type

from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model: Type[CustomUser] = CustomUser
        fields: Tuple[str] = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model: Type[CustomUser] = CustomUser
        fields: Tuple[str] = ('username', 'email')
