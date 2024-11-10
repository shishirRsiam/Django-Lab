from .models import Musician_Model
from django import forms 

class MusicianForm(forms.ModelForm):
    class Meta: 
        model=Musician_Model
        fields='__all__'
        