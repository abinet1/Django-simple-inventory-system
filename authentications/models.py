from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    role_choice = [
        ("Store Admin","Store Admin"),
        ("Store Keeper", "Store Keeper"),
        ("Employee","Employee")
    ]
    role = models.CharField(
        choices=role_choice,
        default="Store Admin",
        max_length=250,
    )

class Supplier(models.Model):
    STATUS = [
        ("Approved","Approved"),
        ("Normalized","Normalized"),
        ("Identified","Identified"),
        ("Invited","Invited"),
        ("Registered","Registered"),
        ("Rejected","Rejected")
    ]
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=50)
    status = models.CharField(choices=STATUS, default="Registered", max_length=50)
    tinNumber = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'