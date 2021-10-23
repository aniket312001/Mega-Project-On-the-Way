from django.db import models
from datetime import datetime

# Create your models here.
class AdminData(models.Model):
    name = models.CharField(max_length=40)
    admin_id = models.IntegerField()
    phone = models.IntegerField()
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=55)

    def __str__(self):
        return self.name



class AdminNotification(models.Model):
    notification = models.CharField(max_length=100000)
    admin = models.ForeignKey(AdminData, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.admin.name