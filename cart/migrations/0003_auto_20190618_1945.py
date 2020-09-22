# Generated by Django 2.2 on 2019-06-18 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20190521_0002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='items',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='product',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='Cartt',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cart.cart'),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='line_total',
            field=models.DecimalField(decimal_places=2, default=10, max_digits=1000),
        ),
    ]
