# Generated by Django 5.0.6 on 2024-05-22 09:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_statement_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=255, unique=True, verbose_name='Почта'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(code='invalid_phone_number', message='Введите телефон в формате +7(XXX)-XXX-XX-XX', regex='\\+7\\(\\d\\d\\d\\)-\\d\\d\\d-\\d\\d-\\d\\d')], verbose_name='Телефон'),
        ),
    ]
