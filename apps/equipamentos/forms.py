from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm, HiddenInput
from .models import Tipo_equipamento, Equipamento


class Tipo_equipamento_form(ModelForm):
    class Meta:
        model = Tipo_equipamento
        fields = '__all__'


class Equipamento_form(ModelForm):
    class Meta:
        model = Equipamento
        fields = '__all__'

        widgets = {
            'usuario': HiddenInput
        }
        labels = {
            'usuario': _(''),
        }