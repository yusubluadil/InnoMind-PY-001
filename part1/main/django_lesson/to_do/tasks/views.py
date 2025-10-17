from datetime import datetime

from django.shortcuts import (
    render,
    redirect
)
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.db.models import Q

from .forms import AddToDoForm, DetailToDoForm
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


def add_to_do(request):
    if request.method == 'POST':
        form = AddToDoForm(data=request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            form.save_m2m()

            return redirect('all_to_do')
    else:
        form = AddToDoForm()

        context = {
            'form': form
        }

        return render(request, 'tasks/add-task.html', context)


def detail_to_do(request, pk):
    obj = Task.objects.filter(id=pk).first()
    if obj is None:
        messages.add_message(request, messages.INFO, 'Məlumat tapılmadı.')
        return redirect('all_to_do')

    form = DetailToDoForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('all_to_do')
    return render(request, 'tasks/detail-task.html', {'form': form})


def delete_to_do(request, pk):
    obj = Task.objects.filter(id=pk).first()
    if obj is None:
        messages.add_message(request, messages.INFO, 'Məlumat tapılmadı.')
        return redirect('all_to_do')

    msg_text = f'{obj.title} adlı To-Do müvəffəqiyyətlə silindi.'
    obj.delete()
    messages.add_message(request, messages.INFO, msg_text)
    return redirect('all_to_do')


def search_to_do(request):
    q = request.GET.get("q")
    searched_data = Task.objects.filter(
        Q(title__icontains=q) |
        Q(description__icontains=q)
    )

    context = {
        'tasks': searched_data
    }

    return render(request, 'tasks/all-tasks.html', context=context)
