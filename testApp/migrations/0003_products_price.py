# Generated by Django 3.1.1 on 2021-05-13 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0002_cart_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='price',
            field=models.IntegerField(default=100),
        ),
    ]
