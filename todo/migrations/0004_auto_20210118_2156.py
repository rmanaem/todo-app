# Generated by Django 3.1 on 2021-01-19 02:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20210118_2116'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='memo',
            new_name='description',
        ),
    ]
