# Generated by Django 3.1 on 2020-08-17 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20200817_1228'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.CharField(default='', max_length=100),
        ),
    ]
