# Generated by Django 3.1.7 on 2021-04-23 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0008_auto_20210423_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server_products',
            name='img',
            field=models.ImageField(upload_to='images'),
        ),
    ]
