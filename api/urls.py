from django.urls import path, include
from rest_framework import routers

from api.views import (
    EmpresaViewSet,
    UserViewSet,
    EquipamentoViewSet,
    PesoViewSet,
    CertificadoViewSet,
    CalibracaoViewSet
)

router = routers.DefaultRouter()
router.register('empresas', EmpresaViewSet)
router.register('equipamentos', EquipamentoViewSet)
router.register('pesos', PesoViewSet)
router.register('certificados', CertificadoViewSet)
router.register('calibracoes', CalibracaoViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
