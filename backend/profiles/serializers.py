from .models import Profile, Building

from djoser.serializers import UserCreateSerializer
from rest_framework import serializers


class SpecialUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'phone_number', 'name', 'building', 'room', 'last_login')


class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = '__all__'

# class UserRegistrationSerializer(UserCreateSerializer):
#     class Meta(UserCreateSerializer.Meta):
#         fields = ('phone_number', 'name', 'building', 'room', 'password', )

# class UserSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)
#
#     class Meta:
#         model = Profile
#         fields = ('id', 'phone_number', 'name', 'building', 'room', 'password', )
#
#     def create(self, validated_data):
#         password = validated_data.pop('password')
#         user = Profile(**validated_data)
#         user.set_password(password)
#         user.save()
#         return user
# from allauth.account.adapter import get_adapter
# from rest_framework import serializers
# from .models import Profile
# # from rest_auth.registration.serializers import RegisterSerializer
#
#
# class ProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Profile
#         fields = ['id', 'phone_number', 'name', 'building', 'room', 'password']
#
#
# class ProfileRegisterSerializer(RegisterSerializer):
#     name = serializers.CharField(required=True, write_only=True)
#     building = serializers.CharField(required=False, write_only=True)
#     room = serializers.CharField(required=False, write_only=True)
#
#     def get_cleaned_data(self):
#         data = super().get_cleaned_data()
#         data['name'] = self.validated_data.get('name', ''),
#         data['building'] = self.validated_data.get('building', ''),
#         data['room'] = self.validated_data.get('room', ''),
#         data['password'] = self.validated_data.get('password', ''),
#         data['phone_number'] = self.validated_data.get('phone_number', ''),
#         return data
#
# # class ProfileRegisterSerializer(RegisterSerializer):
# #     phone_number = serializers.CharField(required=True)
# #     name = serializers.CharField(required=True, write_only=True)
# #     building = serializers.CharField(required=False, write_only=True)
# #     room = serializers.CharField(required=False, write_only=True)
# #
# #     password = serializers.CharField(required=True, write_only=True)
# #     password2 = serializers.CharField(required=True, write_only=True)
# #
# #     def validate_password1(self, password):
# #         return get_adapter().clean_password(password)
# #
# #     def validate(self, data):
# #         if data['password'] != data['password2']:
# #             raise serializers.ValidationError(
# #                 ("Пароли не совпадают."))
# #         return data
# #
# #     def custom_signup(self, request, user):
# #         pass
# #
# #     def get_cleaned_data(self):
# #         return {
# #             'name': self.validated_data.get('name', ''),
# #             'building': self.validated_data.get('building', ''),
# #             'room': self.validated_data.get('room', ''),
# #             'password': self.validated_data.get('password', ''),
# #             'phone_number': self.validated_data.get('phone_number', ''),
# #         }
# #
# #     def save(self, request):
# #         adapter = get_adapter()
# #         user = adapter.new_user(request)
# #         self.cleaned_data = self.get_cleaned_data()
# #         adapter.save_user(request, user, self)
# #         self.custom_signup(request, user)
# #         # setup_user_email(request, user, [])
# #         # return user
# #
# #         user.save()
# #         return user
#
#
# # class CustomRegisterSerializer(RegisterSerializer):
# #     phone_number = serializers.CharField(required=True)
# #     password = serializers.CharField(write_only=True)
# #     name = serializers.CharField(required=True)
# #     building = serializers.CharField(required=True)
# #     room = serializers.CharField(required=True)
# #
# #     def get_cleaned_data(self):
# #         super(CustomRegisterSerializer, self).get_cleaned_data()
# #
# #         return {
# #             "password": self.validated_data.get('password', ''),
# #             "phone_number": self.validated_data.get('phone_number', ''),
# #             "name": self.validated_data.get('name', ''),
# #             "building": self.validated_data.get('building', ''),
# #             "room": self.validated_data.get('room', ''),
# #         }