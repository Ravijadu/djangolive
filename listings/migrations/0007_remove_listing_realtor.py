# Generated by Django 4.1.1 on 2022-10-16 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0006_listing_realtor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='realtor',
        ),
    ]
