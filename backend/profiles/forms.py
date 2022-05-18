from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from .models import Profile, Building


class SignupForm(UserCreationForm):
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Необязательно'}))
    building = forms.ModelChoiceField(queryset=Building.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    room = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Profile
        fields = ['phone_number', 'name', 'building', 'room', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class ProfileChangeForm(UserChangeForm):
    class Meta:
        model = Profile
        fields = ['phone_number', 'name', 'building', 'room', 'password']
