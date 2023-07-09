# Generated by Django 4.2.3 on 2023-07-09 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_forms', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='name',
        ),
        migrations.AddField(
            model_name='person',
            name='usernname',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
