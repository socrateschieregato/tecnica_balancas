from django import forms
from django.forms import ModelForm

from .models import Calibracao, Certificado, Conjunto, Peso


class Pesquisa_form(forms.Form):
    inicio = forms.DateField(
        input_formats=['%d/%m/%Y', '%d/%m/%y'],
        widget=forms.TextInput(
            attrs={'class': 'datepicker1'}
        )
    )
    fim = forms.DateField(
        input_formats=['%d/%m/%Y', '%d/%m/%y'],
        widget=forms.TextInput(
            attrs={'class': 'datepicker2'}
        )
    )


class Calibracao_form(ModelForm):
    class Meta:
        model = Calibracao
        fields = '__all__'
        # widgets = {
        #     'empresa': HiddenInput
        # }
        # labels = {
        #     'empresa': _(''),
        # }


class Certificado_form(ModelForm):
    class Meta:
        model = Certificado
        fields = '__all__'


class Conjunto_form(ModelForm):
    class Meta:
        model = Conjunto
        fields = '__all__'


class Peso_form(ModelForm):
    class Meta:
        model = Peso
        fields = '__all__'
