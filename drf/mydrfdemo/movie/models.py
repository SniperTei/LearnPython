from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    # 类型
    genre = models.CharField(max_length=100)
    # 评分
    rating = models.FloatField()
    # 演员们
    actors = models.CharField(max_length=100)
    # 发布日期
    release_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100)
    updated_by = models.CharField(max_length=100)

    def __str__(self):
        return self.title
