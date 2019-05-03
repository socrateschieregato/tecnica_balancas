from django.shortcuts import render


def tabelas_home(request):
    return render(request, 'home.html')
