from django.db import models

class Movie(models.Model):
  # 电影名字
  title = models.CharField(max_length=255)
  director = models.CharField(max_length=255)
  release_date = models.DateField()
  # 主演
  lead_actor = models.CharField(max_length=255)
  # 公司
  company = models.CharField(max_length=255)
  # 电影类型
  genre = models.CharField(max_length=255)
  rating = models.FloatField()

  def __str__(self):
    return self.title