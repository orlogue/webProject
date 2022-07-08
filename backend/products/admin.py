from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'price', 'quantity', 'created', 'updated']
    list_filter = ['category', 'created', 'updated']
    list_editable = ['price', 'quantity']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
