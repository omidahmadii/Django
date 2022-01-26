from django.db import models

# Create your models here.


class Province(models.Model):
    provice_per_name = models.CharField(max_length=50, verbose_name='نام فارسی')
    provice_eng_name = models.CharField(max_length=50, verbose_name='نام انگلیسی')

    def __str__(self):
        return self.provice_per_name


class Person(models.Model):
    firstname = models.CharField(max_length=50, null=True)
    lastname = models.CharField(max_length=50, null=True)
    fathername = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=15, null=True)
    mobilephone = models.CharField(max_length=15, null=True)
    email = models.EmailField(null = True)
    address = models.CharField(max_length=250, null=True)
    instagram = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=50, null=True)
    province = models.ForeignKey(Province, on_delete=models.SET_NULL, null=True)
    city = models.CharField(max_length=50, null=True)
    job = models.CharField(max_length=50, null=True)
    company = models.CharField(max_length=50, null=True)
    height = models.CharField(max_length=50, null=True)
    weight = models.CharField(max_length=50, null=True)
    gender = models.CharField(max_length=50, null=True)
    pet = models.CharField(max_length=50, null=True)
    Married = models.CharField(max_length=50, null=True)
    father = models.CharField(max_length=50, null=True)
    mothername = models.CharField(max_length=50, null=True)
    mother = models.CharField(max_length=50, null=True)
    natnionalcode = models.CharField(max_length=50, null=True)
    shenasnamehcode = models.CharField(max_length=50, null=True)
    picture = models.CharField(max_length=50, null=True)
    doc = models.CharField(max_length=50, null=True)
    postalcode = models.CharField(max_length=50, null=True)
    brother = models.CharField(max_length=50, null=True)
    sister = models.CharField(max_length=50, null=True)
    car = models.CharField(max_length=50, null=True)
    motorcycle = models.CharField(max_length=50, null=True)
    carno = models.CharField(max_length=50, null=True)
    motorcycleno = models.CharField(max_length=50, null=True)
    childno = models.CharField(max_length=50, null=True)
    child = models.CharField(max_length=50, null=True)
    birthday = models.CharField(max_length=50, null=True)

