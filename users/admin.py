# Register your models here.
from typing import List, Type
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm

from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form: Type[CustomUserCreationForm] = CustomUserCreationForm
    form: Type[CustomUserChangeForm] = CustomUserChangeForm
    model: Type[CustomUser] = CustomUser
    list_display: List[str] = ['username', 'email',]

admin.site.register(CustomUser, CustomUserAdmin)