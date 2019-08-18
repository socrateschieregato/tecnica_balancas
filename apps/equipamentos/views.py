from django.contrib.auth import get_user
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .forms import Equipamento_form
from .models import Equipamento


@login_required
def cad_equip(request):
    usuario = get_user(request)
    form = Equipamento_form(
        request.POST or None,
        initial={'usuario': usuario}
    )
    tipo = 'Cadastro de Equipamento'

    if form.is_valid():
        form.save()

        return render(request, 'equipamentos_home.html', {'tipo': tipo})

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
    equip = Equipamento.objects.all()

    return render(request, 'equipamentos_home.html', {'equip': equip})


@login_required
def del_equip(request, id):
    equip = Equipamento.objects.get(pk=id)

    return render(request, 'equipamentos_home.html', {'equip': equip})
