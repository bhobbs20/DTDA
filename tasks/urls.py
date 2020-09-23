from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [

    # TASKS
    path('', views.tasks, name="tasks"),
    path('create/', views.create_todo, name="create_todo"),

]