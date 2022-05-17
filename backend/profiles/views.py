from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

# Create your views here.
from profiles.forms import SignupForm, LoginForm


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались!')
            return redirect('homepage')
        else:
            messages.error(request, 'Sign up error')
    else:
        form = SignupForm()
    return render(request, 'profiles/signup.html', {'form': form})


def profile_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            profile = form.get_user()
            login(request, profile)
            return redirect('homepage')
    else:
        form = LoginForm()
    return render(request, 'profiles/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('homepage')


def homepage(request):
    return render(request, 'profiles/homepage.html')