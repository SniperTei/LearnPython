from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=50, blank=True)
    mobile = models.CharField(max_length=11, blank=True)
    menu_permissions = models.CharField(max_length=50, blank=True)
    # gender字段默认值是M
    gender = models.CharField(max_length=10, blank=True, default='M') 
    # avatar = models.ImageField(upload_to='avatar/%Y%m%d/', blank=True)
    # add additional fields in here
    def __str__(self):
        return self.username
