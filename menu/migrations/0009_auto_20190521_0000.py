# Generated by Django 2.2 on 2019-05-20 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0008_auto_20190519_1719'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BannerHome',
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='profile/profile_pics'),
        ),
    ]