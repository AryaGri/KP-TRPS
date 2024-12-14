# accounts/forms.py
from django import forms
from .models import Child

class ChildForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = ['parent', 'child']  # Поля модели, которые будут включены в форму

    # Дополнительно можно добавить валидацию или настройку видимости полей
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Можно добавить подсказки или атрибуты HTML для улучшения пользовательского интерфейса
        self.fields['parent'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Выберите родителя'})
        self.fields['child'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Выберите ребенка'})

        # Добавление кастомных сообщений ошибок для полей
        self.fields['parent'].error_messages = {'required': 'Пожалуйста, выберите родителя.'}
        self.fields['child'].error_messages = {'required': 'Пожалуйста, выберите ребенка.'}
