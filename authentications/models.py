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
