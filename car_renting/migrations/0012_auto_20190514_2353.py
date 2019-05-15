# Generated by Django 2.2.1 on 2019-05-14 23:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car_renting', '0011_auto_20190514_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='car',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='car_renting.Car'),
        ),
    ]
