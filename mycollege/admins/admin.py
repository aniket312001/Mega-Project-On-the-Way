from django.contrib import admin
from .models import AdminData, AdminNotification
# Register your models here.

admin.site.register(AdminData)
admin.site.register(AdminNotification)
