from django.urls import path, include
from rest_framework import routers

from api.views import EmpresaViewSet, UserViewSet

router = routers.DefaultRouter()
router.register('empresas', EmpresaViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
