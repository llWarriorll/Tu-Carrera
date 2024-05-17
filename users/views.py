from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.db import IntegrityError
# Create your views here.

def signup(request):
    
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        if request.POST['password1'] == request.POST['password2']:
            #register user
            try:
                user = User.objects.create_user(username=request.POST['email'],
                password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('homeuser')
            except IntegrityError:
                return render(request, 'signup.html',{
                    "error": 'Email Already Exist'
                })
        return render(request, 'signup.html',{
                    "error": 'Password do not match'
                })

def homeuser(request):
    return render(request, 'homeuser.html')