# Generated by Django 4.2 on 2023-05-04 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_dirttype_type_alter_producttype_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
