from django.db import models
import datetime

# Эмоции, которые могут быть использованы в играх
emotions = ['гнев', 'скука', 'радость', 'счастье', 'грусть', 'любовь']

class CUsers(models.Model):
    username = models.CharField('логин', max_length=150)
    name = models.CharField('фио', max_length=150)
    date_of_b = models.DateField('дата рождения')
    role = models.CharField(max_length=20, choices=[
        ('admin', 'Администратор'),
        ('doctor', 'Врач'),
        ('parent', 'Родитель'),
        ('child', 'Ребёнок'),
    ], default='child')
    password = models.CharField('пароль', max_length=150)
    is_auth = models.BooleanField(default=False)

    children = models.ManyToManyField(
        'self',
        symmetrical=False,  # Родитель и ребёнок — разные роли
        related_name='parents',  # Для обратного доступа: child.parents.all()
        blank=True  # Связь может быть пустой
    )

    def __str__(self):
        return f'{self.role} {self.name}'


# Модель для хранения результатов игры
class GameResult(models.Model):
    user = models.ForeignKey(CUsers, on_delete=models.CASCADE)  # Связь с пользователем
    game_type = models.CharField(max_length=20, choices=[
        ('Painting', 'Раскраска'),
        ('Dialog', 'Диалог'),
        ('Choice', 'Выбор'),
    ])  # Тип игры (Painting, Dialog, Choice)
    joy = models.IntegerField(default=0)
    sorrow = models.IntegerField(default=0)
    love = models.IntegerField(default=0)
    anger = models.IntegerField(default=0)
    boredom = models.IntegerField(default=0)
    happiness = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)  # Дата и время игры

    def __str__(self):
        return f"Результат игры {self.game_type} для {self.user.username} - Радость: {self.joy} Счастье: {self.happiness} Любовь: {self.love} Грусть: {self.sorrow} Скука: {self.boredom} Агрессия: {self.anger} "
    
    class Meta:
        verbose_name = "Результат игры"
        verbose_name_plural = "Результаты игр"
        ordering = ['-date']  # Сортировать по дате (от новых к старым)


# Основной класс игры
class Game:
    def __init__(self, game_type, user_id):
        self.game_type = game_type
        self.user_id = user_id
        self.results = []

    def save_result(self, result):
        self.results.append(result)
        # Здесь будет сохранение в БД, если это необходимо
        print(f"Результат игры {self.game_type} для пользователя {self.user_id} сохранён.")


# Классы для конкретных типов игр
class PaintingGame(Game):
    def __init__(self, user_id):
        super().__init__("Painting", user_id)
    
    def calculate_score(self, colors_used):
        scores = {
            'красная': {'гнев': 2},
            'оранжевая': {'гнев': 1, 'радость': 1},
            'жёлтая': {'радость': 2},
            'зелёная': {'счастье': 2},
            'синяя': {'грусть': 1},
            'фиолетовая': {'любовь': 2}
        }

        score = {emotion: 0 for emotion in emotions}

        for color in colors_used:
            if color in scores:
                for emotion, points in scores[color].items():
                    score[emotion] += points
        
        
        result = GameResult(
            user=self.user_id,  # Присваиваем пользователя
            game_type="Painting",
            joy=score['радость'],
            sorrow=score['грусть'],
            love=score['любовь'],
            anger=score['гнев'],
            boredom=score['скука'],
            happiness=score['счастье'],
            
            date=datetime.datetime.now()
        )
        result.save()  # Сохраняем результат в БД


class DialogGame(Game):
    def __init__(self, user_id):
        super().__init__("Dialog", user_id)

    def calculate_score(self, answers):
        answers_scores = {
            'отлично': {'счастье': 2},
            'хорошо': {'радость': 1},
            'нормально': {'скука': 1},
            'прекрасный сон': {'любовь': 2},
            'кошмары': {'гнев': 2},
            'не помню': {'грусть': 1},
            'играл с друзьями': {'счастье': 2},
            'смотрел мультики': {'радость': 2},
            'ничего': {'скука': 1},
            'хочу обнимашки': {'любовь': 2},
            'даже не знаю': {'скука': 1},
            'хочу побыть в одиночестве': {'грусть': 2},
            'весёлых': {'счастье': 2},
            'скучных': {'грусть': 2},
            'одинаково': {'скука': 1}
        }

        score = {emotion: 0 for emotion in emotions}

        for answer in answers:
            if answer in answers_scores:
                for emotion, points in answers_scores[answer].items():
                    score[emotion] += points
        
        result = GameResult(
            user=self.user_id,  # Присваиваем пользователя
            game_type="Dialog",
            joy=score['радость'],
            sorrow=score['грусть'],
            love=score['любовь'],
            anger=score['гнев'],
            boredom=score['скука'],
            happiness=score['счастье'],
            date=datetime.datetime.now()
        )
        result.save()  # Сохраняем результат в БД


class ChoiceGame(Game):
    def __init__(self, user_id):
        super().__init__("Choice", user_id)

    def calculate_score(self, choices):
        choices_scores = {
            'гнев': 2,
            'скука': 1,
            'радость': 2,
            'счастье': 2,
            'грусть': 1,
            'любовь': 2
        }

        score = {emotion: 0 for emotion in emotions}

        for choice in choices:
            if choice in choices_scores:
                score[choice] += choices_scores[choice]
        
        result = GameResult(
            user=self.user_id,  # Присваиваем пользователя
            game_type="Choice",
            joy=score['радость'],
            sorrow=score['грусть'],
            love=score['любовь'],
            anger=score['гнев'],
            boredom=score['скука'],
            happiness=score['счастье'],
            date=datetime.datetime.now()
        )
        result.save()  # Сохраняем результат в БД

# Модель для хранения рецептов
class Prescription(models.Model):
    child = models.ForeignKey(CUsers, on_delete=models.CASCADE, related_name='prescriptions')  # Связь с ребенком
    text = models.TextField('Текст рецепта')  # Текст рецепта
    date_created = models.DateTimeField(auto_now_add=True)  # Дата создания рецепта

    def __str__(self):
        return f"Рецепт для {self.child.username} от {self.date_created.strftime('%Y-%m-%d')}"

    class Meta:
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"
        ordering = ['-date_created']  # Сортировать рецепты по дате (от новых к старым)
