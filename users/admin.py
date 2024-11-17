from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # Fields to display in the admin list view
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'bio', 'profile_picture')

    # Add custom fields to the detail view
    fieldsets = UserAdmin.fieldsets + (
        (_('Additional Info'), {
            'fields': ('bio', 'profile_picture'),
        }),
    )

    # Fields to include when adding a new user
    add_fieldsets = UserAdmin.add_fieldsets + (
        (_('Additional Info'), {
            'fields': ('bio', 'profile_picture'),
        }),
    )
