# Generated by Django 2.2 on 2019-06-26 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20190625_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='buktiPembayaran',
            field=models.FileField(blank=True, upload_to='bukti_pembayaran/'),
        ),
    ]
