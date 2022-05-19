from django.db import models
from .utils import rand_slug
from profiles.models import Profile
from django.urls import reverse
from pytils.translit import slugify

class Category(models.Model):
    name = models.CharField(max_length=200, default="")

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_list_by_category')


class Product(models.Model):
    seller = models.ForeignKey(Profile, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, default="")
    slug = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    count = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail',
                       args=[self.id, self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name + '-' + rand_slug())
        super(Product, self).save(*args, **kwargs)
