from django.shortcuts import render


def tabelas_home(request):
    return render(request, 'tabelas_home.html')
