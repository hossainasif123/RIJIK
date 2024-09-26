from django.contrib import admin
from .models import EmployerProfile

@admin.register(EmployerProfile)
class EmployerProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'company_name', 'contact_number', 'website']
    search_fields = ['company_name', 'user__username']
