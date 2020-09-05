# Generated by Django 3.1 on 2020-09-05 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20200830_2309'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderUpdate',
            fields=[
                ('update_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.CharField(max_length=20)),
                ('update_desc', models.CharField(max_length=500)),
                ('timeStamp', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
