# Generated by Django 2.2 on 2019-07-07 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_cartitem_variation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='line_total',
        ),
    ]
