from django.contrib.auth import get_user
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import Equipamento_form
from .models import Equipamento


@login_required
def cad_equip(request):
    form = Equipamento_form(
        request.POST or None,
        initial={'usuario': get_user(request)}
    )
    tipo = 'Cadastro de Equipamento'

    if form.is_valid():
        form.save()

        return redirect('equip_home')

    return render(
        request,
        'equipamentos_form.html',
        {
            'form': form,
            'tipo': tipo
        }
    )


@login_required
def equip_home(request):
    equipamentos = Equipamento.objects.all()

    return render(request, 'equipamentos_home.html', {'equipamentos': equipamentos})


@login_required
def del_equip(request, id):
    equip = Equipamento.objects.get(pk=id)
    equip.delete()
    equipamentos = Equipamento.objects.all()

    return render(request, 'equipamentos_home.html', {'equipamentos': equipamentos})


@login_required
def upd_equip(request, id):
    pass