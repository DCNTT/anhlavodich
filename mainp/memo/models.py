from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Chat(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(MAX_LENGTH = 255)
    postime = models.DateField(auto_now_add=True)

    class Meta:
        ordering =  ['postime']
        