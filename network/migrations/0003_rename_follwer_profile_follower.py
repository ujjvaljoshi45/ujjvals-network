# Generated by Django 4.0.6 on 2022-07-22 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0002_profile_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='follwer',
            new_name='follower',
        ),
    ]
