from django.contrib import admin
from .models import OrganizationUsers, Positions, EmployeeProfile

admin.site.register(OrganizationUsers)
admin.site.register(Positions)
admin.site.register(EmployeeProfile)
