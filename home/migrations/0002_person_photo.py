# Generated by Django 4.0.1 on 2022-01-23 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='photo',
            field=models.ImageField(null=True, upload_to='home'),
        ),
    ]
