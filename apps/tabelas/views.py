from django.contrib.auth import get_user
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Unidade, Pais, Estado, Municipio
from .forms import Unidade_form, Desvio_form
import json

@login_required
def tabelas_home(request):
    return render(request, 'tabelas_home.html')

@login_required
def cadastro_cidades(request):
    pais = Pais.objects.get_or_create(sigla='BR', pais='Brasil')

    with open('static/cities-br/brazil-cities-states-en.json', encoding="utf-8") as f:
        data = json.load(f)
        for state in data['states']:
            # print(state['uf'], state['name'], state['cities'])
            estado = Estado.objects.get_or_create(sigla=state['uf'], estado=state['name'])

            for city in state['cities']:
                municipio = Municipio.objects.get_or_create(
                    estado=estado[0],
                    municipio=city
                )

    return render(request, 'tabelas_home.html')


def cad_un_medida(request):
    usuario = get_user(request)
    form = Unidade_form(request.POST or None, request.FILES or None, initial={'usuario':usuario})
    tipo = 'Cadastro de Unidades de Medida'

    if form.is_valid():
        form.save()

        return render(request, 'tabelas_home.html', {'tipo': tipo})

    return render(request,
                  'calibracoes_form.html',
                  {
                      'form': form,
                      'tipo': tipo,
                  }
                 )


def cad_desvio(request):
    usuario = get_user(request)
    form = Desvio_form(request.POST or None, request.FILES or None, initial={'usuario':usuario})
    tipo = 'Cadastro de Desvio'

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