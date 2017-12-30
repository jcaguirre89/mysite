# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 17:07:04 2017

@author: crist
"""
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'mysite/signup.html', {'form': form})


def about(request):
    user = request.user
    return render(request, 'mysite/about.html', {'user': user})


def home(request):
    user = request.user
    return render(request, 'mysite/home.html', {'user': user})