from django.urls import path
from . import views


urlpatterns = [
    # Страница регистрации
    path('', views.base_view, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('adm/dashboard/', views.admin_dashboard_view, name='admin_dashboard'),  # Панель администратора
    path('adm/assign_roles/', views.assign_roles_view, name='assign_roles'),     # Назначение ролей
    path('adm/edit_user/<int:user_id>/', views.edit_user_view, name='edit_user'), # Редактирование пользователя
    path('doctor/dashboard/', views.doctor_dashboard_view, name='doctor_dashboard'),  # Панель врача
    path('doctor/patients/', views.patient_list_view, name='patient_list'),    # Список пациентов
    path('doctor/patient/<int:patient_id>/', views.patient_detail_view, name='patient_detail'),  # Детали пациента
    path('doctor/patient/<int:patient_id>/prescription/', views.prescription_form_view, name='prescription_form'), # Создание рецепта
    path('parent/dashboard/', views.parent_dashboard_view, name='parent_dashboard'),  # Панель родителя
    path('parent/child/<int:child_id>/', views.child_detail_view, name='child_detail'), # Детали ребёнка
    path('child/games/', views.game_choice_view, name='choice'),  
    path('child/games/', views.game_dialog_view, name='dialog'), 
    path('child/games/', views.game_painting_view, name='painting'),         # Игры для ребёнка
    path('user/<int:user_id>/', views.user_detail_view, name='user_detail'),
]
