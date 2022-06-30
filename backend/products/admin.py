from django.contrib import admin
from .models import Category, SubCategory, Product, OrderItem, Order


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


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    list_display = ['buyer', 'sent', 'created', 'updated']
    list_filter = ['sent', 'created', 'updated']
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)