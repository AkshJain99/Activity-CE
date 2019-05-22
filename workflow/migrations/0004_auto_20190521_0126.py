# Generated by Django 2.2 on 2019-05-21 08:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0003_merge_20190520_0942'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='costum_color',
        ),
        migrations.AlterField(
            model_name='organization',
            name='theme_color',
            field=models.CharField(default='25ced1', max_length=6, validators=[django.core.validators.RegexValidator(code='nomatch', message='Length has to be 6', regex='^.{6}$')], verbose_name='Organization Costum Color'),
        ),
        migrations.AlterField(
            model_name='program',
            name='gaitid',
            field=models.CharField(blank=True, max_length=255, verbose_name='ID'),
        ),
    ]
