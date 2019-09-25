from django.forms import HiddenInput, ModelForm
from django.utils.translation import gettext_lazy as _

from .models import Empresa, Endereco, Telefone


class Empresa_form(ModelForm):
    class Meta:
        model = Empresa
        fields = '__all__'
        # widgets = {
        #     'empresa': HiddenInput
        # }
        # labels = {
        #     'empresa': _(''),
        # }


class Endereco_form(ModelForm):
    class Meta:
        model = Endereco
        fields = '__all__'
        widgets = {
            'empresa': HiddenInput
        }
        labels = {
            'empresa': _(''),
        }


class Telefone_form(ModelForm):
    class Meta:
        model = Telefone
        fields = '__all__'
        widgets = {
            'empresa': HiddenInput
        }
        labels = {
            'empresa': _(''),
        }
