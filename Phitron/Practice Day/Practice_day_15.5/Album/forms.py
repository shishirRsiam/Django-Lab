from django import forms
from .models import Album_Model


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album_Model
        fields='__all__'
