from django import forms

class pacientesformulario (forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email= forms.EmailField()

class medicosformulario (forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email= forms.EmailField()

class especialidadesformulario (forms.Form):
    nombre = forms.CharField(max_length=40)