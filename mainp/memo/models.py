from enum import auto
from django.db import models
# Create your models here.

class Chat(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(max_length = 255)
    
    postime = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering =  ["-postime"]
