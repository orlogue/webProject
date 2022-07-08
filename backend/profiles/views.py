from rest_framework.permissions import AllowAny
from .serializers import *
from rest_framework import generics


class BuildingsList(generics.ListAPIView):
    queryset = Building.objects.order_by('name')
    serializer_class = BuildingSerializer
    permission_classes = [AllowAny]


class TelegramIDCreate(generics.CreateAPIView):
    queryset = Telegram.objects.all()
    serializer_class = TelegramIDSerializer
    permission_classes = [AllowAny]


class ProfileRetrieve(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = SpecialUserSerializer
    lookup_field = 'phone_number'
    permission_classes = [AllowAny]
