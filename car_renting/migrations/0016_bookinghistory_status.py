# Generated by Django 2.2.1 on 2019-05-19 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_renting', '0015_bookinghistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinghistory',
            name='status',
            field=models.CharField(default='canceled', max_length=255),
        ),
    ]
