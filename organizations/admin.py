from django_tenants.admin import TenantAdminMixin
from .models import Organization
from .models import Domain
from django.contrib import admin


@admin.register(Organization)
class OrganizationAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'created_on', 'schema_name')
    search_fields = ('name',)
    ordering = ('-created_on',)


@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    list_display = ('domain', 'tenant', 'is_primary')
    search_fields = ('domain',)
# Register your models here.
