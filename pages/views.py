from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.db import IntegrityError


def index(request):
    context = {
        'form': UserCreationForm
    }
    return render(request, 'pages/index.html', context)


def register(request):
    if request.method == 'GET':
        return render(request, 'pages/signup.html', {'form':UserCreationForm()})
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