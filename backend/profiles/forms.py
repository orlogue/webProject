from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile


class SignupForm(UserCreationForm):
    phone_number = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Необязательно'}))
    building = forms.IntegerField(widget=forms.RadioSelect(attrs={'class': 'form-control'}))
    room = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Profile
        fields = ['phone_number', 'name', 'building', 'room', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    phone_number = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))