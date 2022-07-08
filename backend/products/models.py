from django.db import models
from pytils.translit import slugify
from .utils import rand_slug
from profiles.models import Profile


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    seller = models.ForeignKey(Profile, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, default='')
    slug = models.SlugField(max_length=200, db_index=True, unique=True, default='')
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name + '-' + rand_slug())
        super(Product, self).save(*args, **kwargs)
