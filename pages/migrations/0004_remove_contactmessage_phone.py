# Generated by Django 5.1.3 on 2024-11-15 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_contactmessage_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactmessage',
            name='phone',
        ),
    ]