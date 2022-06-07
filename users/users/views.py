from django.shortcuts import render, redirect
import requests
import django.middleware.csrf
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from .forms import SignUpForm, LoginForm
from rest_framework.authtoken.models import Token

def login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        print(form)
        if form.is_valid():
            print("si")
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            token = Token.objects.get(user=user)
            if user is not None and token is not None:
                auth_login(request, user)
                return redirect('../users/profile')
            else:
                messages.info(request , 'invalid credentials')
    else:
        form = LoginForm()
    return render(request, '../templates/registration/login.html', {'form':form})

def logout(request):
    auth_logout(request)
    return redirect('../users')

@login_required
def profile(request):
    return render(request, '../templates/profile.html',{'data':request.user.profile})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.name = form.cleaned_data.get('name')
            user.profile.age = form.cleaned_data.get('age')
            user.save()
            Token.objects.create(user=user)
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            auth_login(request, user)
            return redirect('../users/profile')
    else:
        form = SignUpForm()
    return render(request, '../templates/registration/signup.html', {'form': form})