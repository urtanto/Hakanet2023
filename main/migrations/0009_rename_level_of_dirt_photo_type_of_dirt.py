# Generated by Django 4.2 on 2023-05-04 05:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_order_extra_services'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='level_of_dirt',
            new_name='type_of_dirt',
        ),
    ]