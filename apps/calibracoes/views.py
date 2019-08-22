from datetime import date

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .forms import Calibracao_form, Pesquisa_form
from .models import Calibracao


@login_required
def calib_home(request):
    return render(request, 'calibracoes_home.html')


@login_required
def list_calib(request):
    form = Pesquisa_form(request.POST or None)

    if form.is_valid():
        inicio = date(
            int(form.data['inicio'][6:10]),
            int(form.data['inicio'][3:5]),
            int(form.data['inicio'][0:2]),
        )
        fim = date(
            int(form.data['fim'][6:10]),
            int(form.data['fim'][3:5]),
            int(form.data['fim'][0:2]),
        )
        calibracoes = Calibracao.objects.filter(
            dt_calib__gte=inicio,
            dt_calib__lte=fim
        )

        return render(
            request,
            'calibracoes_list.html',
            {'calibracoes': calibracoes}
        )

    return render(request, 'pesquisa_form.html', {'form': form})


@login_required
def cad_calib(request):
    form = Calibracao_form(request.POST or None, request.FILES or None)
    tipo = 'Calibração'

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
