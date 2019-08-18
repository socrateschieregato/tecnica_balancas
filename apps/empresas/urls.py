from django.urls import path

from apps.empresas import views

urlpatterns = [
    path('', views.empresas_home, name='empresas_home'),
    path('cad_empresa/', views.cad_empresa, name='cad_empresa'),
    path('upd_empresa/<int:id>', views.upd_empresa, name='upd_empresa'),
    path('del_empresa/<int:id>', views.del_empresa, name='del_empresa'),
]
