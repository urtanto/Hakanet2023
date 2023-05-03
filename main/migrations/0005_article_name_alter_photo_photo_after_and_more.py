# Generated by Django 4.2 on 2023-05-03 15:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_photo_photo_photo_photo_after_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='name',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='photo',
            name='photo_after',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='photo',
            name='photo_before',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='service',
            name='name',
            field=models.TextField(default=''),
        ),
        migrations.CreateModel(
            name='BlackListToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]