from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Profile, Building

# Register your models here.


class ProfileAdmin(UserAdmin):
    model = Profile
    list_display = ('phone_number', 'name', 'building', 'room', 'is_staff', 'is_active',)
    list_filter = ('phone_number', 'building', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('phone_number', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
    #     ),
    # )
    search_fields = ('phone_number', 'name')
    ordering = ('phone_number', 'name')


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Building)