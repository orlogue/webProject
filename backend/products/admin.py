from django.contrib import admin
from .models import Category, SubCategory, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


admin.site.register(Category, CategoryAdmin)


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category']
    list_filter = ['category']


admin.site.register(SubCategory, SubCategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'price', 'quantity', 'created', 'updated']
    list_filter = ['category', 'created', 'updated']
    list_editable = ['price', 'quantity']
    # prepopulated_fields = {'slug': ('name', )}


admin.site.register(Product, ProductAdmin)
