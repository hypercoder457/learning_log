from typing import Union

from django.contrib.auth import login
from django.contrib.sites.shortcuts import get_current_site
from django.core.handlers.wsgi import WSGIRequest
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.http.response import (HttpResponsePermanentRedirect,
                                  HttpResponseRedirect)
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from .forms import CustomUserCreationForm
from .models import CustomUser
from .tokens import account_activation_token


# Create your views here.
def register(request: WSGIRequest) -> HttpResponse:
    """Register a new user."""
    if request.method != 'POST':
        form = CustomUserCreationForm() # Display blank registration form.
    else:
        form = CustomUserCreationForm(data=request.POST) # Process completed form.
        
        if form.is_valid():
            new_user = form.save(commit=False)
            # This is a FLAG for the user, if the user is active or not.
            new_user.is_active = False
            # This code is for email confirmation.
            new_user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your account for Learning Log!'
            message = render_to_string('acc_active_template.html', {
                'user': new_user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(new_user.pk)),
                'token': account_activation_token.make_token(new_user)
            }) # After rendering this the user will be asked to click a link to confirm their account,
                # Which will lead them to the 'activate' view function to activate their account.
            to_email = form.cleaned_data.get('email')

            # Create a message.
            email = EmailMessage(
                mail_subject,
                message,
                to=[to_email]
            )
            # Send the email and return a response.
            email.send()
            return render(request, 'registration/email_confirmation.html')

    # Display a blank or invalid registration form.
    context = { 'form': form }
    return render(request, 'registration/register.html', context)

def activate(request: WSGIRequest, uidb64: bytes, token: str) -> Union[HttpResponseRedirect, HttpResponsePermanentRedirect, 
HttpResponse]:
    """
    Function for activating the user's account.
    """
    try:
        # Get a user id and get the current user object
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    # Handle the errors that may happen.
    except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        # Set the user is_active flag to True so the user can login.
        user.is_active = True
        user.save()
        # Log the user in, then go back to the home page. The user has successfully been confirmed!!!!!!
        login(request, user)
        return redirect('learning_logs:index')
    else:
        return render(request, 'registration/invalid_link.html')
