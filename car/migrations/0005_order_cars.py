# Generated by Django 5.0.6 on 2024-07-08 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0004_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cars',
            field=models.ManyToManyField(related_name='orders', to='car.car'),
        ),
    ]
