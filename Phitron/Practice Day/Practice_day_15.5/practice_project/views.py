from django.shortcuts import render
from musician.models import Musician_Model
def home(request):
    musician_data=Musician_Model.objects.all()
    print(musician_data)
    return render(request,'home.html',{'data': musician_data})