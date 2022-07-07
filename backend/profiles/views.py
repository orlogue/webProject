from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .models import Profile, Building
from .serializers import *

from rest_framework import generics

from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import FormView
from rest_framework import viewsets, status

# from .forms import SignupForm, LoginForm
# from .serializers import ProfileSerializer, ProfileRegisterSerializer


class BuildingsList(generics.ListAPIView):
    queryset = Building.objects.order_by('name')
    serializer_class = BuildingSerializer
    permission_classes = [AllowAny]


class TelegramIDCreate(generics.CreateAPIView):
    queryset = Telegram.objects.all()
    serializer_class = TelegramIDSerializer
    permission_classes = [AllowAny]

# class ProfileUpdate(generics.UpdateAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileUpdateSerializer
#     permission_classes = [IsAuthenticated]

# class ProfilesList(APIView):
#     def get(self, request, format=None):
#         profiles = Profile.objects.all()
#         serializer = ProfileSerializer(profiles, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, *args, **kwargs):
#         data = {
#             'id': request.user.id,
#             'phone_number': request.data.get('phone_number'),
#             'password': request.data.get('password'),
#             'name': request.data.get('name'),
#             'building': request.data.get('building'),
#             'room': request.data.get('room'),
#         }
#         serializer = ProfileSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# def signup(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             messages.success(request, 'Вы успешно зарегистрировались!')
#             return redirect('homepage')
#         else:
#             messages.error(request, 'Sign up error')
#     else:
#         form = SignupForm()
#     return render(request, 'profiles/signup.html', {'form': form})
#
#
# def profile_login(request):
#     if request.user.is_authenticated:
#         return redirect('homepage')
#     if request.method == 'POST':
#         form = LoginForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('homepage')
#     else:
#         form = LoginForm()
#     return render(request, 'profiles/login.html', {'form': form})
#
# # class LoginView(FormView):
# #     form_class = LoginForm
# #     template_name = 'profiles/login.html'
# #     success_url = reverse_lazy('homepage')
#
#
# def user_logout(request):
#     logout(request)
#     return redirect('homepage')
#
#
# def homepage(request):
#     return render(request, 'profiles/homepage.html')