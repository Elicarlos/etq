from django import forms

class FormSearch(forms.Form):
    buscar = forms.IntegerField(label='Buscar')
