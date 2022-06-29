from django.db import models
from django.urls import reverse
from django.utils.text import slugify
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


    def get_absolute_url(self):
        return reverse('product_list_by_category', args=[self.slug])


class SubCategory(models.Model):
    category = models.ForeignKey(Category, related_name='subcategory', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    seller = models.ForeignKey(Profile, on_delete=models.CASCADE)
    category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, default="")
    slug = models.SlugField(max_length=200, db_index=True, unique=True, default='')
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'
        # return reverse('product_detail',
        #                args=[self.id, self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name + '-' + rand_slug())
        super(Product, self).save(*args, **kwargs)

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000/' + self.image.url
        return ''

    # def get_range(self):
    #     return [(i, str(i)) for i in range(1, self.quantity + 1)]


class Order(models.Model):
    buyer = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    sent = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.pk)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
