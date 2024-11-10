from django.shortcuts import render, redirect
from .forms import MusicianForm
from .models import Musician_Model

def add_musician(request):
    if request.method == 'POST':
        add_musician_form = MusicianForm(request.POST)
        if add_musician_form.is_valid():
            add_musician_form.save()
            return redirect('home_page')
    else:
        add_musician_form = MusicianForm()
    return render(request, 'musician.html', {'form': add_musician_form})

def edit_musician(request, id):
    musician_object = Musician_Model.objects.all().get(pk=id)
    add_musician_form = MusicianForm(instance=musician_object)
    
    if request.method == 'POST':
        add_musician_form = MusicianForm(request.POST, instance=musician_object)
        if add_musician_form.is_valid():
            add_musician_form.save()
            return redirect('home_page')
    
    return render(request, 'musician.html', {'form': add_musician_form})

def delete(request, id):
    delete_musician = Musician_Model.objects.all().get(pk=id).delete()
    return redirect('home_page')
