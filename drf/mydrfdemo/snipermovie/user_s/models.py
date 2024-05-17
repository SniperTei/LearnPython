from django.db import models

class User_S(models.Model):
  # Add your custom fields here
  username = models.CharField(max_length=100)
  email = models.EmailField()
  password = models.CharField(max_length=100)
  date_of_birth = models.DateField(null=True, blank=True)

  # Add any additional methods or properties here
  def __str__(self):
    return self.username