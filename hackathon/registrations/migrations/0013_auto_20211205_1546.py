# Generated by Django 3.1.13 on 2021-12-05 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0012_top_winner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='winner',
            name='id',
        ),
        migrations.AddField(
            model_name='winner',
            name='position',
            field=models.IntegerField(default=1, primary_key=True, serialize=False, unique=True),
            preserve_default=False,
        ),
    ]
