from django import forms

class Calculadora(forms.Form):
    salario = forms.CharField(label="Salario", required=True, widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'Salario'}))
    dias = forms.CharField(label="", required=True, widget = forms.TextInput(attrs={'class':'form-control','placeholder':'Dias'}))
    # solidario = forms.CharField(label="", required=True, widget = forms.TextInput(attrs={'class':'form-control'}))
    # salario_dias = forms.CharField(label="", required=True, widget = forms.TextInput(attrs={'class':'form-control'}))
    # transporte = forms.CharField(label="", required=True, widget = forms.TextInput(attrs={'class':'form-control'}))
    # total_devengado = forms.CharField(label="", required=True, widget = forms.TextInput(attrs={'class':'form-control'}))
    # salud = forms.CharField(label="", required=True, widget = forms.TextInput(attrs={'class':'form-control'}))
    # pension = forms.CharField(label="", required=True, widget = forms.TextInput(attrs={'class':'form-control'}))
    # bono_solidario = forms.CharField(label="", required=True, widget = forms.TextInput(attrs={'class':'form-control'}))
    # base_gravada = forms.CharField(label="", required=True, widget = forms.TextInput(attrs={'class':'form-control'}))
    # renta_excenta = forms.CharField(label="", required=True, widget = forms.TextInput(attrs={'class':'form-control'}))
    # base_retefuente = forms.CharField(label="", required=True, widget = forms.TextInput(attrs={'class':'form-control'}))
    # base_retefuenteuvt = forms.CharField(label="", required=True, widget = forms.TextInput(attrs={'class':'form-control'}))
    # porcentaje_retefuente = forms.CharField(label="", required=True, widget = forms.TextInput(attrs={'class':'form-control'}))