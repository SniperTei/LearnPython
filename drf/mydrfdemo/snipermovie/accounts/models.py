from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
  # email = models.EmailField(unique=True)
  # Add your custom fields here
  bio = models.TextField(blank=True)
  location = models.CharField(max_length=255, blank=True)
  # Add more fields as needed
  account_type = models.CharField(max_length=255, blank=True)

  def __str__(self):
    return self.username