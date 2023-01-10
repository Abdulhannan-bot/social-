# Generated by Django 3.2.16 on 2023-01-02 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0010_rename_account_account_account_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='account_name',
            new_name='full_name',
        ),
        migrations.AddField(
            model_name='account',
            name='email',
            field=models.EmailField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='password',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='user',
            field=models.CharField(default='abc', max_length=100, unique=True),
        ),
    ]