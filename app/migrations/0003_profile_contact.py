# Generated by Django 2.2.16 on 2020-09-12 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_work'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='contact',
            field=models.TextField(default='test', verbose_name='コンタクト'),
            preserve_default=False,
        ),
    ]
