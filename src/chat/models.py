from django.contrib.auth.models import User
from django.db import models


class ChatMessage(models.Model):
    text = models.CharField(max_length=255)
    publication_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')

    class Meta:
        ordering = ['-publication_date']