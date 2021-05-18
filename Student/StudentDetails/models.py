from django.db import models

# Create your models here.
class Students(models.Model):
    name=models.CharField(max_length=100,default='')
    rollnumber=models.IntegerField(unique=True,default='')
    dateofbirth=models.CharField(max_length=100,default='')
    marks=models.IntegerField(max_length=3,default=0)