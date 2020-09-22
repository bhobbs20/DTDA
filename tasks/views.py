from django.shortcuts import render
from .models import Todo


def tasks(request):
    all_tasks = Todo.objects.all()
    context = {
        "all_tasks": all_tasks
    }
    return render(request, 'tasks/task.html', context)
