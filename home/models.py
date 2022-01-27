from django.db import models

# Create your models here.


class Province(models.Model):
    provice_per_name = models.CharField(max_length=50, verbose_name='نام فارسی')
    provice_eng_name = models.CharField(max_length=50, verbose_name='نام انگلیسی')

    def __str__(self):
        return self.provice_per_name


class City(models.Model):
    city_per_name = models.CharField(max_length=50, verbose_name='نام فارسی')
    city_eng_name = models.CharField(max_length=50, verbose_name='نام انگلیسی')

    def __str__(self):
        return self.city_per_name


class Person(models.Model):
    first_name = models.CharField(max_length=50, null=True, verbose_name="نام")
    last_name = models.CharField(max_length=50, null=True, verbose_name="نام خانوادگی")
    mobile = models.CharField(max_length=15, null=True, verbose_name="تلفن همراه")
    telephone = models.CharField(max_length=15, null=True, verbose_name="تلفن ثابت")
    email = models.EmailField(null=True, verbose_name="ایمیل")
    birth_day = models.DateField(null=True, verbose_name="تاریخ تولد")
    gender = models.BooleanField(null=True, verbose_name="حنسیت")
    natnional_code = models.CharField(max_length=10, null=True, verbose_name="کد ملی")
    shenasnameh_code = models.CharField(max_length=10, null=True, verbose_name="شماره شناسنامه")
    height = models.DecimalField(max_digits=3, decimal_places=0, null=True, verbose_name="قد")
    weight = models.DecimalField(max_digits=4, decimal_places=1, null=True, verbose_name="وزن")
    instagram = models.CharField(max_length=50, null=True, verbose_name="ای دی اینستاگرام")
    province = models.ForeignKey(Province, on_delete=models.SET_NULL, null=True, verbose_name="استان")
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, verbose_name="شهر")
    postalcode = models.DecimalField(max_digits=15, decimal_places=0, null=True, verbose_name="کد پستی")
    address = models.TextField(null=True, verbose_name="نشانی")
    father = models.CharField(max_length=50, null=True, verbose_name="نام پدر")
    mother = models.CharField(max_length=50, null=True, verbose_name="نام مادر")
    married = models.BooleanField(default=False, verbose_name="متاهل")
    pet = models.CharField(max_length=50, null=True, verbose_name="حیوان خانگی")
    job = models.CharField(max_length=50, null=True, verbose_name="شغل")
    company = models.CharField(max_length=50, null=True, verbose_name="شرکت")
    #doc = models.CharField(max_length=50, null=True)
    # picture = models.CharField(max_length=50, null=True)
    # country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, default='ایران')
    #car = models.CharField(max_length=50, null=True)
    #motorcycle = models.CharField(max_length=50, null=True)
    #carno = models.CharField(max_length=50, null=True)
    #motorcycleno = models.CharField(max_length=50, null=True)
    #child = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name