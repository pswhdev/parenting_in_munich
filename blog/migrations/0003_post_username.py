# Generated by Django 5.0.6 on 2024-05-25 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_post_slug_alter_post_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='username',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
