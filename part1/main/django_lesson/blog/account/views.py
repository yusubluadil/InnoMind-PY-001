from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .forms import RegisterForm, LoginForm


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            messages.error(request, form.errors)
            return redirect('register')
    else:
        form = RegisterForm()

        context = {'form': form}
        return render(request, 'auth/register.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username') # renad
        password = request.POST.get('password') # 123

        if not User.objects.filter(username=username).exists():
            messages.error(request, 'İstifadəçi adı yanlışdır')
            return redirect('login')

        user = authenticate(username=username, password=password)

        if user is None:
            # Display an error message if authentication fails (invalid password)
            messages.error(request, "Şifrə yanlışdır")
            return redirect('login')
        else:
            # Log in the user and redirect to the home page upon successful login
            login(request, user)
            return redirect('all_blogs')
    else:
        form = LoginForm()
        
        context = {"form": form}
        return render(request, 'auth/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('all_blogs')
