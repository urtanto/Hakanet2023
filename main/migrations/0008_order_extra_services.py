# Generated by Django 4.2 on 2023-05-04 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_order_taken'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='extra_services',
            field=models.TextField(default=''),
        ),
    ]