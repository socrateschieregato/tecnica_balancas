from django.shortcuts import render


def empresas_home(request):
    return render(request, 'empresas_home.html')
