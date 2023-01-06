from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    incoming = models.PositiveIntegerField(default=0)  # 음수일 수 없음
    spending = models.PositiveIntegerField(default=0)  # 음수일 수 없음
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)