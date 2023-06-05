from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate 
from django.contrib.auth import login as auth_login

def login(request):
    if request.method == 'POST':
        usrname = str(request.POST['username'])
        pswd = str(request.POST['password'])

        user = authenticate(username=usrname, password=pswd)

        if user is not None:
            auth_login(request, user)
            return redirect('home')

        return render(request, 'login_system/index.html')
    else:
        return render(request, 'login_system/index.html')