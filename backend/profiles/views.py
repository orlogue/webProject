from .models import Profile

from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import FormView
from rest_framework import viewsets

from profiles.forms import SignupForm, LoginForm
from profiles.serializers import ProfileSerializer


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
    if request.user.is_authenticated:
        return redirect('homepage')
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('homepage')
    else:
        form = LoginForm()
    return render(request, 'profiles/login.html', {'form': form})

# class LoginView(FormView):
#     form_class = LoginForm
#     template_name = 'profiles/login.html'
#     success_url = reverse_lazy('homepage')


def user_logout(request):
    logout(request)
    return redirect('homepage')


def homepage(request):
    return render(request, 'profiles/homepage.html')


class ProfilesViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
