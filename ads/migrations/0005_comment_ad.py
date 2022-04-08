# Generated by Django 3.2.6 on 2022-04-06 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0004_remove_comment_ad'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='ad',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ads.ad'),
            preserve_default=False,
        ),
    ]
