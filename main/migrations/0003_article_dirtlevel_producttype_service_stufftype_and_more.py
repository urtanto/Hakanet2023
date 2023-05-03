# Generated by Django 4.2 on 2023-05-03 08:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_user_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='DirtLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('cost', models.FloatField()),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='StuffType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TimeType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='super_user',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='ReviewForCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='')),
                ('level_of_dirt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.dirtlevel')),
                ('type_of_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.producttype')),
                ('type_of_stuff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.stufftype')),
                ('type_of_time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.timetype')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField()),
                ('level_of_dirt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.dirtlevel')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.service')),
                ('type_of_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.producttype')),
                ('type_of_stuff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.stufftype')),
                ('type_of_time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.timetype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CommentForArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]