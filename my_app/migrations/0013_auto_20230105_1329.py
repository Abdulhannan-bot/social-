# Generated by Django 3.2.16 on 2023-01-05 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0012_comment_profile_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='profile_pic',
        ),
        migrations.AddField(
            model_name='account',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
