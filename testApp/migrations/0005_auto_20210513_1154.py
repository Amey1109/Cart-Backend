# Generated by Django 3.1.1 on 2021-05-13 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0004_auto_20210513_1148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='count',
        ),
        migrations.AddField(
            model_name='products',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]