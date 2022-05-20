from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'quantity', 'created', 'updated']
    list_filter = ['created', 'updated']
    list_editable = ['price', 'quantity']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)
