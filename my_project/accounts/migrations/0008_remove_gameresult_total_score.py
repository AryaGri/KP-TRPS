# Generated by Django 4.2.6 on 2024-12-20 00:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_gameresult_game_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gameresult',
            name='total_score',
        ),
    ]
