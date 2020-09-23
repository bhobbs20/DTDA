from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm


def tasks(request):
    all_tasks = Todo.objects.all()
    context = {
        "all_tasks": all_tasks
    }
    return render(request, 'tasks/task.html', context)


def create_todo(request):
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html', {'form': TodoForm()})
    else:
        try:
            form = TodoForm(request.POST)
            new_todo = form.save(commit=False)
            new_todo.user = request.user
            new_todo.save()
            return redirect('tasks:tasks')
        except ValueError:
            return render(request, 'tasks/create_task.html',
                          {'form': TodoForm(), 'error': 'Bad data passed in. Try again.'})
