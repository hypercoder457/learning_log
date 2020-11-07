from django.shortcuts import render, redirect
from django.contrib.auth import login

from .forms import CustomUserCreationForm

from django.http import HttpResponse

from django_email_verification import sendConfirm
# Create your views here.
def register(request) -> HttpResponse:
    """Register a new user."""
    if request.method != 'POST':
        form = CustomUserCreationForm() # Display blank registration form.
    else:
        form = CustomUserCreationForm(data=request.POST) # Process completed form.
        
        if form.is_valid():
            new_user = form.save()
            sendConfirm(new_user)
            # Log the user in, then redirect back to the home page.
            login(request, new_user)
            return redirect('learning_logs:index')

    # Display a blank or invalid registration form.
    context = { 'form': form }
    return render(request, 'registration/register.html', context)