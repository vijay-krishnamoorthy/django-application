from django.db import models

# Create your models here.
class register(models.Model):
    title=models.CharField(max_length=250)
    author=models.CharField(max_length=250)
    subject=models.CharField(max_length=250)
    description=models.CharField(max_length=1000)
    published=models.BooleanField(default=False)

