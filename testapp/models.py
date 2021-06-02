from django.db import models

# Create your models here.

class Employee(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    city=models.CharField(max_length=20)
    address=models.TextField()



#model based forms

#if we are creating the form based on the model