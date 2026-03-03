from django.contrib import admin

from .models import Organization


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("name", "domain", "timezone", "is_active", "created_at")
    search_fields = ("name", "domain")
    list_filter = ("is_active", "created_at")
