# Generated by Django 4.2.4 on 2023-09-07 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_userprofile_user_img'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]