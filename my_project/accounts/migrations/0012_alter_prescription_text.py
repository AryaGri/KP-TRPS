# Generated by Django 4.2.6 on 2024-12-20 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_alter_prescription_options_alter_prescription_child'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescription',
            name='text',
            field=models.CharField(max_length=300, verbose_name='пароль'),
        ),
    ]
