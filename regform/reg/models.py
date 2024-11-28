from django.db import models

# Create your models here.
class Reg(models.Model):
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    email = models.EmailField()
    phno = models.IntegerField()
    qualification = models.CharField(max_length=200)
