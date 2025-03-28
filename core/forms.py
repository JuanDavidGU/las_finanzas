from django import forms

class Calculadora(forms.Form):
    salario = forms.CharField(label="Salario", required=True, widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'Salario'}))
    dias = forms.CharField(label="", required=True, widget = forms.TextInput(attrs={'class':'form-control','placeholder':'Dias'}))
    hora_extra_diurna = forms.CharField(label="Hora Extra Diurna", required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Hora Extra Diurna'}))
    hora_extra_nocturna = forms.CharField(label="Hora Extra Nocturna", required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Hora Extra Nocturna'}))
    hora_extra_dominical_festiva_diurna = forms.CharField(label="Hora Extra Dominical/Festiva Diurna", required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Hora Extra Dominical/Festiva Diurna'}))
    hora_extra_dominical_festiva_nocturna = forms.CharField(label="Hora Extra Dominical/Festiva Nocturna", required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Hora Extra Dominical/Festiva Nocturna'}))
    