# Generated by Django 5.0.6 on 2024-06-12 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='event',
            unique_together={('name', 'description', 'location', 'time', 'date')},
        ),
    ]
