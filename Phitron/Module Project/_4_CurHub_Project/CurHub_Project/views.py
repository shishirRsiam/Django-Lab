from django.shortcuts import redirect, render

def home(request):
    context = {
        'projects' : [1, 2, 3, 4, 5],
    }
    return render(request, 'home.html', context)

def view_info(request):
    context = {
        'projects' : [1, 2, 3, 4, 5],
    }
    return render(request, 'view_info.html', context)