from pyexpat.errors import messages
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect


from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.cache import never_cache
from .forms import ChildForm
from .models import Child

@never_cache
@csrf_protect
def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        role = request.POST['role']

        # Проверка совпадения паролей
        if password.strip() != confirm_password.strip():
            messages.error(request, 'Пароли не совпадают.')
            return render(request, 'register.html')

        # Проверка на уникальность пользователя
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Пользователь с таким именем уже существует.')
            return render(request, 'register.html')

        # Создание нового пользователя
        user = User.objects.create_user(username=username, password=password)
        user.profile.role = role  # Предполагается, что у модели User есть профиль с ролью
        user.save()

        # Вход после успешной регистрации
        login(request, user)

        # Перенаправление в зависимости от роли
        if role == 'doctor':
            return redirect('doctor_dashboard')
        elif role == 'admin':
            return redirect('admin_dashboard')
        elif role == 'parent':
            return redirect('parent_dashboard')
        elif role == 'child':
            return redirect('game_dashboard')

    return render(request, 'register.html')
@never_cache
@csrf_protect

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            
            # Получение роли пользователя
            try:
                role = user.profile.role  # Предполагается, что у вас есть модель Profile с ролью пользователя
            except AttributeError:
                # Если у пользователя нет роли, перенаправить на страницу с ошибкой
                messages.error(request, 'Ошибка: У этого пользователя нет роли.')
                return redirect('login')
            
            # Перенаправление в зависимости от роли
            if role == 'doctor':
                return redirect('doctor_dashboard')
            elif role == 'admin':
                return redirect('admin_dashboard')
            elif role == 'parent':
                return redirect('parent_dashboard')
            elif role == 'child':
                return redirect('game_dashboard')
            else:
                messages.error(request, 'Неизвестная роль пользователя.')
                return redirect('login')
        else:
            messages.error(request, 'Неверные учетные данные. Попробуйте снова.')
    
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('home')

# Рендеринг главной страницы администратора
def doctor_dashboard_view(request):
    return render(request, 'doctor_dashboard.html')

# Рендеринг главной страницы администратора
def admin_dashboard_view(request):
    return render(request, 'admin_dashboard.html')

def base_view(request):
    return render(request, 'main.html')

# Рендеринг страницы для назначения ролей
def assign_roles_view(request):
    return render(request, 'assign_roles.html')

# Рендеринг страницы редактирования пользователя
def edit_user_view(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'edit_user.html', {'user': user})

# Рендеринг страницы для отображения списка пациентов врача
def patient_list_view(request):
    # Пример получения пациентов
    patients = User.objects.filter(role='patient')  # Например, пациенты имеют роль 'patient'
    return render(request, 'patient_list.html', {'patients': patients})

# Рендеринг страницы для детального просмотра пациента
def patient_detail_view(request, patient_id):
    patient = get_object_or_404(User, id=patient_id)
    return render(request, 'patient_detail.html', {'patient': patient})

# Рендеринг страницы для родителей, где они видят детей
from .models import Child

def parent_dashboard_view(request):
    # Получаем всех детей для текущего пользователя
    children = Child.objects.filter(parent=request.user)

    # Если у родителя нет детей, показываем сообщение
    if not children.exists():
        message = "У вас пока нет детей."
    else:
        message = None  # Если дети есть, сообщение не нужно

    # Отправляем данные в шаблон
    return render(request, 'parent_dashboard.html', {'children': children, 'message': message})
    # Отправляем данные в шаблон
    return render(request, 'parent_dashboard.html', {'children': children, 'message': message})

# Рендеринг страницы для пользователя
def user_detail_view(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'user_detail.html', {'user': user})

def prescription_form_view(request):
    return render(request, 'prescription_form.html')

def child_detail_view(request):
    return render(request, 'child_detail.html')

def game_choice_view(request):
    return render(request, 'game_choice.html')

def game_dialog_view(request):
    return render(request, 'game_dialog.html')

def game_painting_view(request):
    return render(request, 'game_painting.html')

def add_child_view(request):
    if request.method == 'POST':
        # Получаем ID выбранного ребенка из формы
        child_id = request.POST.get('child_id')
        parent = request.user  # Текущий пользователь — родитель

        try:
            # Получаем пользователя с выбранным ID
            child = User.objects.get(id=child_id, profile__role='child')
            # Добавляем ребенка родителю
            Child.objects.create(parent=parent, child=child)
            messages.success(request, f'{child.username} добавлен как ваш ребенок.')
            return redirect('parent_dashboard')
        except User.DoesNotExist:
            messages.error(request, 'Ошибка: выберите правильного ребенка.')
            return redirect('add_child')

    # Получаем всех пользователей с ролью "child"
    children = User.objects.filter(profile__role='child')
    return render(request, 'add_child.html', {'children': children})