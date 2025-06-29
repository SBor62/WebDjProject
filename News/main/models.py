from django.contrib.auth.models import User
from django.db import models

class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Автор",
        null=True  # Временно разрешаем NULL
    )

    def __str__(self):
        return self.title
