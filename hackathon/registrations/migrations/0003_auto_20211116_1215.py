# Generated by Django 3.1.13 on 2021-11-16 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0002_registrations_team_members'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='registrations',
            options={'verbose_name': 'Registration', 'verbose_name_plural': 'Registrations'},
        ),
        migrations.AlterField(
            model_name='registrations',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Team Leader'),
        ),
    ]
