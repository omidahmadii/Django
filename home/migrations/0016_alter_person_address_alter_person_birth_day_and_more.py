# Generated by Django 4.0.1 on 2022-01-27 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_alter_province_provice_eng_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='address',
            field=models.TextField(blank=True, null=True, verbose_name='نشانی'),
        ),
        migrations.AlterField(
            model_name='person',
            name='birth_day',
            field=models.DateField(blank=True, null=True, verbose_name='تاریخ تولد'),
        ),
        migrations.AlterField(
            model_name='person',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.city', verbose_name='شهر'),
        ),
        migrations.AlterField(
            model_name='person',
            name='company',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='شرکت'),
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='ایمیل'),
        ),
        migrations.AlterField(
            model_name='person',
            name='father',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='نام پدر'),
        ),
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.BooleanField(blank=True, null=True, verbose_name='حنسیت'),
        ),
        migrations.AlterField(
            model_name='person',
            name='height',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=3, null=True, verbose_name='قد'),
        ),
        migrations.AlterField(
            model_name='person',
            name='instagram',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='ای دی اینستاگرام'),
        ),
        migrations.AlterField(
            model_name='person',
            name='job',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='شغل'),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='نام خانوادگی'),
        ),
        migrations.AlterField(
            model_name='person',
            name='mobile',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='تلفن همراه'),
        ),
        migrations.AlterField(
            model_name='person',
            name='mother',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='نام مادر'),
        ),
        migrations.AlterField(
            model_name='person',
            name='natnional_code',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='کد ملی'),
        ),
        migrations.AlterField(
            model_name='person',
            name='pet',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='حیوان خانگی'),
        ),
        migrations.AlterField(
            model_name='person',
            name='postalcode',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=15, null=True, verbose_name='کد پستی'),
        ),
        migrations.AlterField(
            model_name='person',
            name='province',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.province', verbose_name='استان'),
        ),
        migrations.AlterField(
            model_name='person',
            name='shenasnameh_code',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='شماره شناسنامه'),
        ),
        migrations.AlterField(
            model_name='person',
            name='telephone',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='تلفن ثابت'),
        ),
        migrations.AlterField(
            model_name='person',
            name='weight',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True, verbose_name='وزن'),
        ),
    ]
