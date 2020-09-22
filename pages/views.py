from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError


def index(request):
    context = {
        'form': UserCreationForm
    }
    return render(request, 'pages/index.html', context)


def register(request):
    if request.method == 'GET':
        return render(request, 'pages/signup.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('main:index')
            except IntegrityError:
                return render(request, 'pages/signup.html', {'form': UserCreationForm(),
                                                             'error': 'That username has already been taken. Please choose a new username'})
        else:
            return render(request, 'pages/signup.html',
                          {'form': UserCreationForm(), 'error': 'Passwords did not match'})


def login_user(request):
    if request.method == 'GET':
        return render(request, 'pages/login_user.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'pages/login_user.html',
                          {'form': AuthenticationForm(), 'error': 'Username and password did not match'})
        else:
            login(request, user)
            return redirect('main:index')


def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('main:index')
