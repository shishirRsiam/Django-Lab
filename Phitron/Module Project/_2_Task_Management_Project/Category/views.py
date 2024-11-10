from django.shortcuts import redirect, render
from .models import CategoryForms

def add_category(request):
    if request.method == 'POST':
        forms = CategoryForms(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('/')

    form = CategoryForms()
    context = {
        'form': form,
    }
    return render(request, 'add_category.html', context)