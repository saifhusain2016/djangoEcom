# Generated by Django 3.1 on 2020-08-30 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20200823_1818'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_info', models.CharField(max_length=5000)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=500)),
                ('address2', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zip_code', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
            ],
        ),
    ]