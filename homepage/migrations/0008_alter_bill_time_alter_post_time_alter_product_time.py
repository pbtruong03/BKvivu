# Generated by Django 4.2.4 on 2023-12-07 17:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0007_alter_bill_time_alter_post_time_alter_product_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 8, 0, 40, 48, 993726)),
        ),
        migrations.AlterField(
            model_name='post',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 8, 0, 40, 48, 993726)),
        ),
        migrations.AlterField(
            model_name='product',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 8, 0, 40, 48, 993726)),
        ),
    ]
