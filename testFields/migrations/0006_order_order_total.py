# Generated by Django 3.1.1 on 2021-05-14 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testFields', '0005_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_total',
            field=models.IntegerField(default=100),
        ),
    ]
