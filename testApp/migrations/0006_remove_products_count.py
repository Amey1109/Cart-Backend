# Generated by Django 3.1.1 on 2021-05-13 06:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0005_auto_20210513_1154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='count',
        ),
    ]