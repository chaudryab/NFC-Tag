# Generated by Django 3.2.4 on 2021-06-28 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_users_forget_password_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='month',
            field=models.IntegerField(default=12),
        ),
    ]