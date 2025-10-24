from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

from .forms import RegisterForm


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' welcome {username} !!')
            return redirect('all_to_do')
        else:
            messages.info(request, f'account done not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form':form, 'title':'log in'})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print(form.errors)
    else:
        form = RegisterForm()

        context = {
            'form': form
        }
        return render(request, 'accounts/register.html', context)


def profile(request):
    user_profile = request.user.profile

    context = {
        'user_profile': user_profile
    }
    return render(request, 'accounts/profile.html', context)


def logout_view(request):
    logout(request)
    return redirect('all_to_do')

