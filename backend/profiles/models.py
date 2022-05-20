from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models
# Create your models here.


class ProfileManager(BaseUserManager):
    def create_user(self, phone_number, password, **extra_fields):
        if not phone_number:
            raise ValueError(_('Введите номер телефона'))
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone_number, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(phone_number, password, **extra_fields)
        # Гоша, не грусти)))


class Profile(AbstractUser):
    username = None
    email = None
    phone_number = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    building = models.ForeignKey('Building', on_delete=models.CASCADE, null=True)
    room = models.SmallIntegerField(blank=False, default=0)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = ProfileManager()

    def __str__(self):
        return self.phone_number


class Building(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Корпус'
        verbose_name_plural = 'Корпусы'


