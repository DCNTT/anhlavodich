from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password1 = models.CharField(max_length=30)
    password2 = models.CharField(max_length=30)


    def __str__(self):
        return self.username + " "  + self.password1 

    class Meta:
        db_table ="users"