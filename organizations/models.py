from django.db import models
from django_tenants.models import TenantMixin, DomainMixin

class Organization(TenantMixin):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    picture = models.ImageField(upload_to='organization_pictures/', blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    auto_create_schema = True  # Auto-create tenant schema

    def __str__(self):
        return self.name


class Domain(DomainMixin):
    pass
