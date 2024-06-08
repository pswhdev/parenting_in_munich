# Generated by Django 5.0.6 on 2024-06-08 09:02

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('image', cloudinary.models.CloudinaryField(default='https://res.cloudinary.com/daluxpssk/image/upload/v1717835739/placeholderimage_ujh6em.svg', max_length=255, verbose_name='image')),
            ],
        ),
    ]