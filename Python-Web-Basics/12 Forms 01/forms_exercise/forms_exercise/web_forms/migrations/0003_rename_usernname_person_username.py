# Generated by Django 4.2.3 on 2023-07-09 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_forms', '0002_remove_person_name_person_usernname_alter_person_age'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='usernname',
            new_name='username',
        ),
    ]
