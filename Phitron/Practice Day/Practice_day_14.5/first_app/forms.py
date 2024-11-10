from django import forms
from django.forms.widgets import NumberInput

class ExampleForm(forms.Form):
    name = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)
    text_attrs = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))
    email = forms.EmailField()
    Agree = forms.BooleanField(label='Agree')
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    birthday = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))

    BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
    date_choise = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))

    FAVORITE_COLORS_CHOICES = [
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('black', 'Black'),
    ]
    favorite_color = forms.ChoiceField(widget=forms.RadioSelect(), choices=FAVORITE_COLORS_CHOICES)
    colors_multiple = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(), choices=FAVORITE_COLORS_CHOICES)
