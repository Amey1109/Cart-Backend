# Generated by Django 3.1.1 on 2021-05-15 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testFields', '0006_order_order_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(related_name='_order_products_+', to='testFields.Order'),
        ),
    ]
