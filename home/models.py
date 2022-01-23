from django.db import models

# Create your models here.


class Person(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    Phone = models.CharField(max_length=15)
    email = models.EmailField()
    #gender = models.BooleanField()
    #photo = models.ImageField(upload_to='home/Persons', null=True)
