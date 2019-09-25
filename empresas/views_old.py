from django.contrib.auth import get_user
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404, redirect, render

from tabelas.models import Estado, Municipio, Pais

from .forms import Empresa_form, Endereco_form, Telefone_form
from .models import Empresa, Endereco, Telefone


@login_required
def empresas_home(request):
    empresas = Empresa.objects.all()
    return render(request, 'empresas_home.html', {'empresas': empresas})


@login_required
def cad_empresa(request):
    cidade = Municipio.objects.get(municipio='Franca')
    pais = Pais.objects.get(pais='Brasil')
    uf = Estado.objects.get(estado='São Paulo')

    form_empresa = Empresa_form(
        request.POST or None,
        initial={'user': get_user(request)}
    )
    form_endereco = Endereco_form(
        request.POST or None,
        request.FILES or None,
        initial={'cidade': cidade, 'uf': uf, 'pais': pais}
    )
    form_telefone = Telefone_form(request.POST or None, request.FILES or None)

    if form_empresa.is_valid():
        empresa = form_empresa.save()

        dados = form_empresa.data
        cidade = Municipio.objects.get(id=dados['municipio'])
        pais = Pais.objects.get(id=dados['pais'])
        uf = Estado.objects.get(id=dados['uf'])

        endereco = Endereco(
            tipo_log=dados['tipo_log'], endereco=dados['endereco'],
            bairro=dados['bairro'], numero=dados['numero'],
            cep=dados['cep'], pais=pais, municipio=cidade,
            uf=uf, empresa=empresa
        )
        telefone = Telefone(
            tipo=dados['tipo'], ddd=dados['ddd'],
            num_tel=dados['num_tel'], empresa=empresa
        )

        endereco.save()
        telefone.save()
        return redirect('empresas_home')

    return render(
        request,
        'templates/empresas_form.html',
        {
            'form_empresa': form_empresa,
            'form_endereco': form_endereco,
            'form_telefone': form_telefone
        }
    )


@login_required
def upd_empresa(request, id):

    empresa = get_object_or_404(Empresa, pk=id)
    endereco = get_object_or_404(Endereco, empresa=empresa)
    telefone = get_object_or_404(Telefone, empresa=empresa)

    form_empresa = Empresa_form(request.POST or None, instance=empresa)
    form_endereco = Endereco_form(request.POST or None, instance=endereco)
    form_telefone = Telefone_form(request.POST or None, instance=telefone)

    if form_empresa.is_valid() and form_endereco.is_valid() and form_telefone:
        form_empresa.save()
        form_endereco.save()
        form_telefone.save()
        return redirect('empresas_home')

    return render(
        request,
        'empresas_form.html',
        {
            'form_empresa': form_empresa,
            'form_endereco': form_endereco,
            'form_telefone': form_telefone
        }
    )


@user_passes_test(lambda u: u.is_superuser)
def del_empresa(request, id):
    empresa = get_object_or_404(Empresa, pk=id)

    if request.method == 'POST':
        empresa.delete()
        return redirect('empresas_home')

    return render(request, 'empresas_del.html', {'empresa': empresa})
