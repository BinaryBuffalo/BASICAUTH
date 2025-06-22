from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from .forms import MyForm
from django.db import IntegrityError
from django.contrib import messages
from django.contrib.messages import constants as messages_constants


def registerPage(request):
    result = ""  # Initialize the result variable as an empty string

    try:
        if request.method == "POST":
            form = MyForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')
                email = form.cleaned_data.get('email')

                try:
                    user = User.objects.create_user(username=username, password=password, email=email)
                    user = authenticate(request, username=username, password=password)
                    result = "Registration successful. You are now logged in|green"  # Update result for success
                except IntegrityError as e:
                    if "UNIQUE constraint failed: auth_user.username" in str(e):
                        result = "This username already exists|yellow"
                    else:
                        raise  # Re-raise the exception for other IntegrityError cases
            else:
                error_messages = []
                for field, errors in form.errors.items():
                    error_messages.extend(errors)
                error_message = '\n'.join(error_messages)
                result = 'Captcha was incorrect|red'
        else:
            form = MyForm()

        message, color = "", ""  # Initialize message and color as empty strings

        if result:
            # Split the result into message and color only if result is not empty
            message, color = result.split("|")
    except Exception as e:
        # Handle other exceptions or log them as needed
        print(f"An exception occurred: {e}")
        raise

    return render(request, 'registration/register.html', {'form': form, 'message': message, 'color': color})

def login_view(request):
    error_message = ""
    color = "red"
    
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                # Redirect to the /category/home/ URL after a successful login
                return redirect('/category/home/')
            else:
                error_message = "Username/Password failed."
                color = "yellow"
        else:
            error_message = "Captcha failed."
    else:
        form = MyForm()
    
    return render(request, 'registration/login.html', {'form': form, 'message': error_message, 'color': color})

def Logout(request):
    logout(request)
    return redirect('/')