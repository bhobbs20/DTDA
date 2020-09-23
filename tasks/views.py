from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required


@login_required
def tasks(request):
    all_tasks = Todo.objects.filter(user=request.user, date_completed__isnull=True)
    context = {
        "all_tasks": all_tasks
    }
    return render(request, 'tasks/task.html', context)


@login_required
def completed_todos(request):
    todos = Todo.objects.filter(user=request.user, date_completed__isnull=False).order_by('date_completed')
    return render(request, 'tasks/complete_task.html', {'todos': todos})


@login_required
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


@login_required
def viewtodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'GET':
        form = TodoForm(instance=todo)
        return render(request, 'tasks/viewtodo.html', {'todo': todo, 'form': form})
    else:
        try:
            form = TodoForm(request.POST, instance=todo)
            form.save()
            return redirect('tasks:tasks')
        except ValueError:
            return render(request, 'tasks/viewtodo.html', {'todo': todo, 'form': form, 'error': 'Bad info'})


@login_required
def complete_task(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        todo.date_completed = timezone.now()
        todo.save()
        return redirect('tasks:tasks')


@login_required
def delete_task(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        todo.delete()
        return redirect('tasks:tasks')
