from django.urls import path
from .views import register_view, login_view, logout_view, dashboard_view, task_list, task_create, task_update, task_delete

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard_view, name='dashboard'),
    
    # CRUD operations for tasks
    path('task_list/', task_list, name='task_list'),
    path('tasks/create/', task_create, name='task_create'),
    path('tasks/update/<int:id>/', task_update, name='task_update'),
    path('tasks/delete/<int:id>/', task_delete, name='task_delete'),
]
