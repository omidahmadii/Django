# Generated by Django 4.0.1 on 2022-01-27 04:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_rename_phone_person_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_per_name', models.CharField(max_length=50, verbose_name='نام فارسی')),
                ('city_eng_name', models.CharField(max_length=50, verbose_name='نام انگلیسی')),
            ],
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provice_per_name', models.CharField(max_length=50, verbose_name='نام فارسی')),
                ('provice_eng_name', models.CharField(max_length=50, verbose_name='نام انگلیسی')),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='Married',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='birthday',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='brother',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='car',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='carno',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='child',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='company',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='doc',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='father',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='gender',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='height',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='instagram',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='job',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='mobile',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='mother',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='motorcycle',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='motorcycleno',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='natnionalcode',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='pet',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='picture',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='postalcode',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='shenasnamehcode',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='sister',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='weight',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='firstname',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='lastname',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.city'),
        ),
        migrations.AddField(
            model_name='person',
            name='province',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.province'),
        ),
    ]
