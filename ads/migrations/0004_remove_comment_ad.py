# Generated by Django 3.2.6 on 2022-04-06 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0003_auto_20220406_1701'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='ad',
        ),
    ]
