# Generated by Django 3.1.1 on 2021-05-16 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testFields', '0012_order_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_completed',
            field=models.BooleanField(default=False),
        ),
    ]