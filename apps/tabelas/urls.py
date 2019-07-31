from django.urls import path, include
from apps.tabelas import views


urlpatterns = [
    path('', views.tabelas_home, name='tabelas_home'),
    path('add/', views.cadastro_cidades, name='cadastro_cidades'),
    path('add_unidade/', views.cad_un_medida, name='cad_un_medida'),
    path('cad_desvio/', views.cad_desvio, name='cad_desvio'),
]