from django.urls import path

from empresas import views
from empresas import views_old

urlpatterns = [
    path('', views_old.empresas_home, name='empresas_home'),
    path('v1/empresas/', views.EmpresaListCreate.as_view()),
    path('cad_empresa/', views_old.cad_empresa, name='cad_empresa'),
    path('upd_empresa/<int:id>', views_old.upd_empresa, name='upd_empresa'),
    path('del_empresa/<int:id>', views_old.del_empresa, name='del_empresa'),
]
