from django.db import models

# Create your models here.
class Register(models.Model):
    title=models.CharField(max_length=250)
    author=models.CharField(max_length=250)
    subject=models.CharField(max_length=250)
    description=models.CharField(max_length=1000)
    date_published = models.DateTimeField(auto_now=True,auto_now_add=False)
    likes = models.BigIntegerField

    def __str__(self):
        return self.author 

class LoginData(models.Model):
    title = models.CharField(max_length=250)
    author=models.CharField(max_length=250)
    subject=models.CharField(max_length=250)
    description=models.CharField(max_length=1000)
    date_published = models.DateTimeField(auto_now=True,auto_now_add=False)
    likes = models.BigIntegerField
