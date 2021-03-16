# Generated by Django 3.1.7 on 2021-02-25 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('login_user', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True, verbose_name='Логин')),
                ('password', models.CharField(max_length=41, verbose_name='Пароль')),
                ('First_Name', models.TextField(verbose_name='Имя')),
                ('user_bio', models.TextField(verbose_name='Фамилия')),
            ],
        ),
    ]
