from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UseeLoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login


def user_register(request):
    if request.method =='POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(cd['username'], cd['email'], cd['password'] )
            messages.success(request, 'user Registered Successfully', 'success')
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})



def user_login(request):
    if request.method =='POST':
        form = UseeLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, ['username'], cd['password'] )
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged In  Successfully', 'success')
                return redirect('home')
            else:
                messages.error(request, 'Username Or Password is Wrong', 'danger')
    else:
        form = UseeLoginForm()
    return render(request, 'login.html', {'form': form})
