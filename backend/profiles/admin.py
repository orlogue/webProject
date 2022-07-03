from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Profile, Building

# Register your models here.


class ProfileAdmin(UserAdmin):
    model = Profile
    list_display = ('id', 'phone_number', 'name', 'building', 'room', 'is_staff', 'is_active',)
    list_filter = ('phone_number', 'building', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('phone_number', 'password', 'building', 'room')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
    #     ),
    # )
    # list_editable = ('phone_number', 'name', 'building', 'room')
    search_fields = ('phone_number', 'name')
    ordering = ('phone_number', 'name')


class BuildingAdmin(admin.ModelAdmin):
    model = Building
    list_display = ['id', 'name']


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Building, BuildingAdmin)