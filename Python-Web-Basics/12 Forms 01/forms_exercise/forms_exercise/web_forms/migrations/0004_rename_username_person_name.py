# Generated by Django 4.2.3 on 2023-07-09 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_forms', '0003_rename_usernname_person_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='username',
            new_name='name',
        ),
    ]
