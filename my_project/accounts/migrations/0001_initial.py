# Generated by Django 4.2.6 on 2024-12-18 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150, verbose_name='логин')),
                ('name', models.CharField(max_length=150, verbose_name='фио')),
                ('date_of_b', models.DateTimeField(verbose_name='дата рождения')),
                ('role', models.CharField(choices=[('admin', 'Администратор'), ('doctor', 'Врач'), ('parent', 'Родитель'), ('child', 'Ребёнок')], default='child', max_length=20)),
                ('password', models.CharField(max_length=150, verbose_name='пароль')),
            ],
        ),
    ]
