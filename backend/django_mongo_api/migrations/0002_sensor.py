# Generated by Django 4.0.4 on 2022-04-21 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_mongo_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.IntegerField(default=25)),
                ('moisture', models.IntegerField(default=50)),
                ('humidity', models.IntegerField(default=50)),
                ('air_vent', models.BooleanField(default=True)),
                ('water_pump', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'sensor',
            },
        ),
    ]