from datetime import datetime

from django.shortcuts import (
    render,
    redirect
)
from django.shortcuts import get_object_or_404
from django.contrib import messages

from .models import Task


def all_to_do(request):
    user = request.user
    # user_tasks = Task.objects.filter(user=user)
    if user.is_authenticated:
        user_tasks = user.tasks.all()
    else:
        user_tasks = []

    context = {
        'tasks': user_tasks
    }

    return render(request, 'tasks/all-tasks.html', context=context)


def change_status_to_in_progress(request, pk):
    if request.method == 'POST':
        task_obj = get_object_or_404(Task, pk=pk)
        if task_obj.status == 'I':
            messages.add_message(request, messages.INFO, 'Status İn Progress-dir.')
            return redirect('all_to_do')
        else:
            messages.add_message(request, messages.INFO, 'Status müvəffəqiyyətlə dəyişdi.')

        task_obj.status = 'I'
        task_obj.start_date = datetime.now()
        task_obj.save()

    return redirect('all_to_do')


def change_status_to_done(request, pk):
    if request.method == 'POST':
        task_obj = get_object_or_404(Task, pk=pk)
        if task_obj.status == 'D':
            messages.add_message(request, messages.INFO, 'Status Done-dir.')
            return redirect('all_to_do')
        else:
            messages.add_message(request, messages.INFO, 'Status müvəffəqiyyətlə dəyişdi.')

        task_obj.status = 'D'
        task_obj.completed_date = datetime.now()
        task_obj.save()

    return redirect('all_to_do')

