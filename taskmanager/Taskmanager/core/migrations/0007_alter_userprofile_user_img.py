# Generated by Django 4.2.4 on 2023-09-07 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_userprofile_user_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
