from django.shortcuts import render

from . import form

def home(request):

    forms = {
        'form' : form.MyForm
    }

    return render(request, './home.html', forms)

