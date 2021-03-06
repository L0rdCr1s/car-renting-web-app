# Generated by Django 2.2.1 on 2019-05-14 13:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('plate_number', models.CharField(max_length=8)),
                ('availability', models.CharField(max_length=15)),
                ('price', models.CharField(max_length=8)),
                ('location', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=300)),
                ('cover_image', models.ImageField(upload_to='cars/%Y/%m/%d/')),
                ('registered_at', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to=settings.AUTH_USER_MODEL, verbose_name='car owner')),
            ],
            managers=[
                ('cars', django.db.models.manager.Manager()),
            ],
        ),
    ]
