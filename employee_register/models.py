from django.db import models

# Create your models here.

class position(models.Model):
    title = models.CharField(max_length=100)


class employee(models.Model):

    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=255)
    mobile =models.CharField(max_length=20)
    position = models.ForeignKey(position,on_delete=models.CASCADE)
