from django.shortcuts import redirect, render

from Category.models import Category
from . import STATIC_DATABASE
from . import models

def show_task(request):
    text = 'My Tasks'
    forms = models.TaskForms()
    Tasks = models.Task.objects.all().order_by('id')
    if not Tasks:
        text = 'Empty Tasks'
    context = {
        'text' : text,
        'forms' : forms,
        'Tasks' : Tasks, 
    }
    return render(request, 'show_task.html', context)

def add_task(request):
    # Save_To_Database()
    if request.method == 'POST':
        forms = models.TaskForms(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('home')

    form = models.TaskForms()
    context = {
        'header_content' : 'Add Task',
        'btn_name' : 'Submit',
        'form' : form,
    }
    return render(request, 'add_task.html', context)

def edit_task(request, id):
    Task = models.Task.objects.get(pk = id)
    if request.method == 'POST':
        form = models.TaskForms(request.POST, instance = Task)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    form = models.TaskForms(instance = Task)
    context = {
        'header_content' : 'Edit Task',
        'btn_name' : 'Save',
        'form' : form,
    }
    return render(request, 'add_task.html', context)

def delete_task(request, id):
    Task = models.Task.objects.get(pk = id)
    Task.delete()
    
    return redirect('home')


# Extra Code for debug
def Save_To_Database():
    for task_data in STATIC_DATABASE.TASK_DATA:
        # Get or create categories for each task
        categories = [Category.objects.get_or_create(name=cat_name)[0] for cat_name in task_data['categories']]
        
        # Create or update the task
        task, created = models.Task.objects.update_or_create(
            taskTitle=task_data['taskTitle'],
            defaults={
                'taskDescription': task_data['taskDescription'],
                'is_completed': task_data['is_completed'],
            }
        )
        
        # Assign the categories to the task
        task.category.set(categories)
        task.save()

    print("Tasks loaded successfully.")