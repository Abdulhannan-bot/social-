# Generated by Django 3.2.16 on 2023-01-10 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0026_alter_comment_post_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
