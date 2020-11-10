from typing import Tuple, Type
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model: Type[CustomUser] = CustomUser
        fields: Tuple[str] = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model: Type[CustomUser] = CustomUser
        fields: Tuple[str] = ('username', 'email')