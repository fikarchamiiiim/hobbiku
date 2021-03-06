# Generated by Django 2.2 on 2019-04-15 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judulMenu', models.CharField(max_length=225)),
                ('descMenu', models.TextField()),
                ('picMenu', models.CharField(max_length=225)),
                ('hargaMenu', models.IntegerField(default='0')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Transaksi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('JudulMenu', models.CharField(max_length=100)),
                ('Jumlah', models.IntegerField()),
                ('pemesan', models.CharField(default='Admin', max_length=100)),
                ('alamat', models.TextField()),
                ('tanggal', models.DateTimeField(auto_now_add=True)),
                ('hargaperSatuan', models.IntegerField(default=0)),
                ('totalHarga', models.IntegerField(default=0)),
            ],
        ),
    ]
