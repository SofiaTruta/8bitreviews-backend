# Generated by Django 4.2.7 on 2023-11-22 19:38

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='cover_url',
            new_name='image_url',
        ),
        migrations.RenameField(
            model_name='game',
            old_name='genre',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='game',
            name='title',
        ),
        migrations.AddField(
            model_name='game',
            name='genres',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), blank=True, default=['no genre'], size=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='game',
            name='release_date',
            field=models.DateTimeField(),
        ),
    ]
