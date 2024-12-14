from django.db import models
from django.contrib.auth.models import User

# Модель профиля для хранения дополнительной информации о пользователе
class Profile(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Администратор'),
        ('doctor', 'Врач'),
        ('parent', 'Родитель'),
        ('child', 'Ребёнок'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='parent')
    date_of_birth = models.DateField(null=True, blank=True)  # Пример: дата рождения, если это важно для ребенка
    full_name = models.CharField(max_length=100, null=True, blank=True)  # Имя, для использования в карточке пользователя

    def __str__(self):
        return f'{self.user.username} - {self.role}'

# Сигнал для автоматического создания профиля, когда создается новый пользователь
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

from django.db import models
from django.contrib.auth.models import User

class Child(models.Model):
    parent = models.ForeignKey(User, on_delete=models.CASCADE)  # Родитель (ссылка на User)
    full_name = models.CharField(max_length=200)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.full_name

