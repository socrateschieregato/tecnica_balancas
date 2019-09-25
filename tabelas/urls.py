from django.urls import path

from tabelas import views

urlpatterns = [
    path('', views.tabelas_home, name='tabelas_home'),
    path('cidades/', views.cadastro_cidades, name='cadastro_cidades'),
    path('add_unidade/', views.cad_un_medida, name='cad_un_medida'),
    path('upd_unidade/<int:id>/', views.upd_unidade, name='upd_unidade'),
    path('del_unidade/<int:id>/', views.del_unidade, name='del_unidade'),
    path('cad_desvio/', views.cad_desvio, name='cad_desvio'),
]
