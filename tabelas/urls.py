from django.urls import path

from tabelas import views

urlpatterns = [
    path('', views.tabelas_home, name='tabelas_home'),
    path('cidades/', views.cadastro_cidades, name='cadastro_cidades'),
]
