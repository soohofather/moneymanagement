from django.db import models
from config import settings
import datetime

# Create your models here.


class Article(models.Model):
    date = models.DateField(("Date"), default=datetime.date.today)
    title = models.CharField(max_length=20)
    content = models.TextField(blank=True)
    incoming = models.PositiveIntegerField(default=0)  # 음수일 수 없음
    spending = models.PositiveIntegerField(default=0)  # 음수일 수 없음
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
