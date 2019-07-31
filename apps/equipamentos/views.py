from django.contrib.auth import get_user
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import  Equipamento, Tipo_equipamento
from .forms import Equipamento_form, Tipo_equipamento_form


@login_required
def cad_equip(request):
    usuario = get_user(request)
    form = Equipamento_form(request.POST or None, request.FILES or None, initial={'usuario':usuario})
    tipo = 'Cadastro de Equipamento'

    if form.is_valid():
        form.save()

        return render(request, 'calibracoes_home.html', {'tipo': tipo})

    return render(request,
                  'calibracoes_form.html',
                  {
                      'form': form,
                      'tipo': tipo,
                  }
                 )

@login_required
def equip_home(request):
    equip = Equipamento.objects.all()

    return render(request, 'equipamentos_home.html', {'equip':equip})


@login_required
def del_equip(request, id):
    equip = Equipamento.objects.get(pk=id)

    return render(request, 'equipamentos_home.html', {'equip':equip})
