# Generated by Django 4.2.1 on 2023-05-28 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='city_image',
            field=models.ImageField(upload_to='media/'),
        ),
    ]