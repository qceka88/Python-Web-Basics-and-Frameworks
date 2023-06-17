# Generated by Django 4.2.2 on 2023-06-17 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NotesApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='content',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='note',
            name='image_url',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]
