from django import forms
from django.forms import ModelForm
from .models import *


class Estado_form(ModelForm):
    class Meta:
        model = Estado
        fields = '__all__'
        # widgets = {
        #     'empresa': HiddenInput
        # }
        # labels = {
        #     'empresa': _(''),
        # }


class Cargo_form(ModelForm):
    class Meta:
        model = Cargo
        fields = '__all__'


class Departamento_form(ModelForm):
    class Meta:
        model = Departamento
        fields = '__all__'


class Municipio_form(ModelForm):
    class Meta:
        model = Municipio
        fields = '__all__'


class Pais_form(ModelForm):
    class Meta:
        model = Pais
        fields = '__all__'


class Grupo_Empresas_form(ModelForm):
    class Meta:
        model = Grupo_Empresas
        fields = '__all__'


class Usuario_form(ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'


class Unidade_form(ModelForm):
    class Meta:
        model = Unidade
        fields = '__all__'


class Desvio_form(ModelForm):
    class Meta:
        model = Desvio
        fields = '__all__'