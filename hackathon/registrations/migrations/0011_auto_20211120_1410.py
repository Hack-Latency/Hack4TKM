# Generated by Django 3.1.13 on 2021-11-20 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0010_faq_sponsors'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='faq',
            options={'ordering': ['order'], 'verbose_name': 'FAQ', 'verbose_name_plural': 'FAQs'},
        ),
        migrations.AlterModelOptions(
            name='sponsors',
            options={'ordering': ['order'], 'verbose_name': 'Sponsor', 'verbose_name_plural': 'Sponsors'},
        ),
    ]
