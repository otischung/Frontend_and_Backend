from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # ForeignKey: 關連到另一張表; CASCADE: 連動刪除
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=300)

    def __str__(self):
        return f"{self.author.username}: {self.content[:20]}"
