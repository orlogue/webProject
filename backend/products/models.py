from django.db import models
from profiles.models import Profile


class Category(models.Model):
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title


class Product(models.Model):
    seller = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='products')
    title = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    count = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

