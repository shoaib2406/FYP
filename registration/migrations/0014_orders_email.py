# Generated by Django 3.1.7 on 2021-05-03 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0013_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]
