# Generated by Django 2.2.16 on 2020-09-26 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_selfskill_software_technical'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Selfskill',
        ),
        migrations.DeleteModel(
            name='Software',
        ),
    ]
