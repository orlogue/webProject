from .models import Profile, Building, Telegram
from rest_framework import serializers


class SpecialUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'phone_number', 'name', 'building', 'room', 'last_login')


class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['name', 'building', 'room']


class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = '__all__'


class TelegramIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telegram
        fields = '__all__'
