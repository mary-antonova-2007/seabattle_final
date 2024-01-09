from django.shortcuts import render, redirect
from .forms import UserRegisterForm, CustomAuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('main')  # или другой URL, куда вы хотите перенаправить пользователя
            else:
                messages.error(request, 'Неверное имя пользователя или пароль')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})


def logout(request):
    auth_logout(request)
    return redirect('login')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Аккаунт {username} был успешно создан!')
            return redirect('login')  # предполагается, что у вас есть URL с именем 'login'
    else:
        form = UserRegisterForm()
    return render(request, 'auth/register.html', {'form': form})

