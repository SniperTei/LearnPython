from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    publisher = models.CharField(max_length=100)
    pubdate = models.DateField()
    # 类型(0: 未知, 1: 科幻, 2: 悬疑, 3: 爱情, 4: 惊悚, 5: 恐怖, 6: 励志, 7: 历史, 8: 传记, 9: 其他)
    type = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100)
    updated_by = models.CharField(max_length=100)

    def __str__(self):
        return self.title