# Generated by Django 4.0.4 on 2022-06-08 04:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_mark_marked_profile_mark_profile_delete_profilemark'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mark',
            name='profile',
        ),
    ]
