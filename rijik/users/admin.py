from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User

class UserAdmin(BaseUserAdmin):
    # Display fields in the list view of the User model in the Django admin
    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'is_staff', 'is_active')
    
    # Fields used to filter the list view of the User model
    list_filter = ('role', 'is_staff', 'is_active', 'is_superuser')

    # Fields displayed when editing a User instance
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Role and Permissions'), {
            'fields': ('role', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    # Fields displayed when creating a new User instance
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'role', 'is_active', 'is_staff', 'is_superuser'),
        }),
    )

    # Fields used to search for users
    search_fields = ('username', 'email', 'first_name', 'last_name')

    # Default ordering of the list view
    ordering = ('username',)

    # Fields used in the raw ID filter
    filter_horizontal = ('groups', 'user_permissions')

# Register the custom User model and the custom UserAdmin class
admin.site.register(User, UserAdmin)
