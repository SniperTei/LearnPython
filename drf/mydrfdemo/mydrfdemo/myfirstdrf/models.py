# from django.db import models
# from django.contrib.auth.models import AbstractUser

# class MyUser(AbstractUser):
#   email = models.EmailField(unique=True)
#   # 电话号码
#   mobile = models.CharField(max_length=11, unique=True)
#   # 生日
#   birthday = models.DateField(null=True, blank=True)
#   # 性别
#   # gender = models.CharField(max_length=6, choices=())
#   # 头像
#   # avatar = models.ImageField(upload_to='avatar/', null=True, blank=True)

#   def __str__(self):
#     return self.username