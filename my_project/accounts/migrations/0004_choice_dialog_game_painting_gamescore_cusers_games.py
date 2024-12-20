# Generated by Django 4.2.6 on 2024-12-19 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_cusers_doctor_children'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='choice_images/')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Изображение для выбора',
                'verbose_name_plural': 'Изображения для выбора',
            },
        ),
        migrations.CreateModel(
            name='Dialog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Фраза для диалога',
                'verbose_name_plural': 'Фразы для диалога',
            },
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название игры')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание игры')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Игра',
                'verbose_name_plural': 'Игры',
            },
        ),
        migrations.CreateModel(
            name='Painting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='paintings/')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Картинка для раскраски',
                'verbose_name_plural': 'Картинки для раскраски',
            },
        ),
        migrations.CreateModel(
            name='GameScore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('joy', models.IntegerField(default=0, verbose_name='Радость')),
                ('sadness', models.IntegerField(default=0, verbose_name='Грусть')),
                ('love', models.IntegerField(default=0, verbose_name='Любовь')),
                ('anger', models.IntegerField(default=0, verbose_name='Гнев')),
                ('boredom', models.IntegerField(default=0, verbose_name='Скука')),
                ('happiness', models.IntegerField(default=0, verbose_name='Счастье')),
                ('date_played', models.DateTimeField(auto_now_add=True)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='game_scores', to='accounts.game')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='game_scores', to='accounts.cusers')),
            ],
            options={
                'verbose_name': 'Результат игры',
                'verbose_name_plural': 'Результаты игры',
            },
        ),
        migrations.AddField(
            model_name='cusers',
            name='games',
            field=models.ManyToManyField(blank=True, related_name='children', to='accounts.game'),
        ),
    ]
