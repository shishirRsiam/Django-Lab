from django.shortcuts import render, redirect
from .forms import AlbumForm
from .models import Album_Model

def add_album(request):
    if request.method == 'POST':
        add_album_form = AlbumForm(request.POST)
        if add_album_form.is_valid():
            add_album_form.save()
            return redirect('home_page')
    else:
        add_album_form = AlbumForm()
    return render(request, 'album.html', {'form': add_album_form})

def edit_album(request, id):
    album_data = Album_Model.objects.all().get(pk=id)
    add_album_form = AlbumForm(instance=album_data)
    
    if request.method == 'POST':
        add_album_form = AlbumForm(request.POST, instance=album_data)
        if add_album_form.is_valid():
            add_album_form.save()
            return redirect('home_page')
    
    return render(request, 'album.html', {'form': add_album_form})
