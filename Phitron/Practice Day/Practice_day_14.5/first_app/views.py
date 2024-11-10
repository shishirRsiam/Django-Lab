from django.shortcuts import render,redirect
from . import forms
# Create your views here.
def home(request):
    if request.method=='POST':
        form=forms.ExampleForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect('home_page')
    else:
        form=forms.ExampleForm()
    return render(request,'home.html',{'form':form})
