# Generated by Django 4.2 on 2023-05-04 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_delete_blacklisttoken'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='taken',
            field=models.BooleanField(default=False),
        ),
    ]
