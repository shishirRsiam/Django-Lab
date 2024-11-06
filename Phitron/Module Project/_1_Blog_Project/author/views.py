from django.shortcuts import redirect, render
from .forms import AuthorForms
# from . import forms

def home(request):
    if request.method == 'POST':
        author_form = AuthorForms(request.POST)
        if author_form.is_valid():
            author_form.save()
            print("&_&"*30)
            print('Form Save Done...')
            return redirect('/')

    author_form = AuthorForms()
    # return render(request, 'author/author.html')
    return render(request, 'author/author.html', {'form' : author_form})

