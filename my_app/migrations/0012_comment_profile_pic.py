# Generated by Django 3.2.16 on 2023-01-02 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0011_auto_20230102_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
