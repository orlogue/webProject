from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
# Create your models here.


class Profile(AbstractBaseUser):
    phone_number = models.IntegerField()
    name = models.CharField(max_length=100)
    building = models.ForeignKey('Building', on_delete=models.CASCADE)
    room = models.SmallIntegerField()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['building', 'room']

    def __str__(self):
        return str(self.phone_number)


class Building(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

