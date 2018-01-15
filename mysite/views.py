# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 17:07:04 2017

@author: crist
"""
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts/login/')
def myhome(request, username):
    user = User.objects.get(username=username)
    return render(request, 'mysite/myhome.html', {'user': user})


def validate_username(request):
    username = request.GET.get('username',None)
    data = {
            'is_taken': User.objects.filter(username__iexact=username).exists()
            }
    if data['is_taken']:
        data['message'] = 'Username taken'
    else:
        data['message'] = 'Username available'
    return JsonResponse(data)

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