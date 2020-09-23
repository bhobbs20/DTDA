from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [

    # TASKS
    path('', views.tasks, name="tasks"),
    path('create/', views.create_todo, name="create_todo"),
    path('<int:todo_pk>', views.viewtodo, name='viewtodo'),
    path('<int:todo_pk>/complete', views.complete_task, name='complete_task'),
    path('<int:todo_pk>/delete', views.delete_task, name='delete_task'),
    path('completed/', views.completed_todos, name='completed_todos'),

]