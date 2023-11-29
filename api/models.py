from django.db import models

# Create your models here.
class Programmer(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    is_active = models.BooleanField(default=True)