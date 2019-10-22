from django.urls import path, include
from rest_framework import routers

from api.views import (
    EmpresaViewSet,
    UserViewSet,
    EquipamentoViewSet,
    DesvioViewSet,
    PesoViewSet,
    CertificadoViewSet,
    CalibracaoViewSet
)

router = routers.DefaultRouter()
router.register('empresas', EmpresaViewSet)
router.register('equipamentos', EquipamentoViewSet)
router.register('desvio', DesvioViewSet)
router.register('peso', PesoViewSet)
router.register('certificado', CertificadoViewSet)
router.register('calibracao', CalibracaoViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
