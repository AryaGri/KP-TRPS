# Generated by Django 4.2.6 on 2024-12-19 00:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_cusers_delete_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cusers',
            name='doctor_children',
        ),
    ]
