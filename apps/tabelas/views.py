import json

from django.contrib.auth import get_user
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404, redirect, render

from .forms import Desvio_form, Unidade_form
from .models import Estado, Municipio, Pais, Unidade


@login_required
def tabelas_home(request):
    return render(request, 'tabelas_home.html')


@user_passes_test(lambda u: u.is_superuser)
def cadastro_cidades(request):
    Pais.objects.get_or_create(sigla='BR', pais='Brasil')

    with open(
            'static/cities-br/brazil-cities-states-en.json',
            encoding="utf-8"
    ) as f:
        data = json.load(f)
        for state in data['states']:
            estado = Estado.objects.get_or_create(
                sigla=state['uf'],
                estado=state['name']
            )

            for city in state['cities']:
                Municipio.objects.get_or_create(
                    estado=estado[0],
                    municipio=city
                )

    return render(request, 'tabelas_home.html')


def cad_un_medida(request):
    usuario = get_user(request)
    form = Unidade_form(
        request.POST or None,
        initial={'usuario': usuario}
    )
    tipo = 'Cadastro de Unidades de Medida'
    unidades = Unidade.objects.all()

    if form.is_valid():
        form.save()
        form = Unidade_form(
            request.POST or None,
            request.FILES or None,
            initial={'usuario': usuario}
        )
        return render(
            request,
            'unidade_form.html',
            {'form': form, 'unidades': unidades}
        )

    return render(
        request,
        'unidade_form.html',
        {
            'form': form,
            'tipo': tipo,
            'unidades': unidades
        }
    )


@login_required
def upd_unidade(request, id):

    unidade = get_object_or_404(Unidade, pk=id)
    form = Unidade_form(
        request.POST or None,
        instance=unidade
    )

    if form.is_valid():
        form.save()

        return redirect('cad_un_medida')

    return render(
        request,
        'unidade_form.html',
        {
            'form': form
        }
    )


@user_passes_test(lambda u: u.is_superuser)
def del_unidade(request, id):
    deletar = get_object_or_404(Unidade, pk=id)

    if request.method == 'POST':
        deletar.delete()
        return redirect('tabelas_home')

    return render(request, 'confirm_del.html', {'deletar': deletar})


def cad_desvio(request):
    usuario = get_user(request)
    form = Desvio_form(
        request.POST or None,
        request.FILES or None,
        initial={'usuario': usuario}
    )
    tipo = 'Cadastro de Desvio'

    if form.is_valid():
        form.save()

        return render(request, 'calibracoes_home.html', {'tipo': tipo})

    return render(
        request,
        'calibracoes_form.html',
        {
            'form': form,
            'tipo': tipo,
        }
    )
