from django.db import models
from profiles.models import Profile


class Category(models.Model):
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title




class Product(models.Model):
    seller = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    price = models.IntegerField()
    count = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


STATUS_CHOICES = (
    ('sent', 'sent'),
    ('approved', 'approved')
)


class RelationshipManager(models.Manager):
    def invatations_received(self, receiver):
        qs = Relationship.objects.filter(receiver=receiver, status='send')
        return qs


class Relationship(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='receiver')
    status = models.CharField(max_length=16, choices=STATUS_CHOICES)
    product = models.IntegerField


    objects = RelationshipManager()

    def __str__(self):
        return f"{self.sender}-{self.receiver}-{self.status}"
