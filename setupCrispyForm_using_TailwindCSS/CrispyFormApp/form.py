from django import forms

class MyForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100)
    email = forms.EmailField(label="Email")
    message = forms.CharField(label="Message")

    OPTIONS = [
        ('1', 'One'),
        ('2', 'Two'),
        ('3', 'Three'),
    ]
    cls = forms.ChoiceField(choices=OPTIONS, label="Select Option")
