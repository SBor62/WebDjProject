
# main/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Можно добавить свои поля, например:
    age = models.PositiveIntegerField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
