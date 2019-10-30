from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from api.serializers import (
    EmpresaSerializer,
    UserSerializer,
    EquipamentoSerializer,
    PesoSerializer,
    CertificadoSerializer,
    CalibracaoSerializer
)
from calibracoes.models import Peso, Certificado, Calibracao
from empresas.models import Empresa
from equipamentos.models import Equipamento

token = (TokenAuthentication, )
permission = (IsAuthenticated, )


class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    authentication_classes = token
    permission_classes = permission
    lookup_field = "cpf_cnpj"


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class EquipamentoViewSet(viewsets.ModelViewSet):
    queryset = Equipamento.objects.all()
    serializer_class = EquipamentoSerializer
    authentication_classes = token
    permission_classes = permission


class PesoViewSet(viewsets.ModelViewSet):
    queryset = Peso.objects.all()
    serializer_class = PesoSerializer
    authentication_classes = token
    permission_classes = permission


class CertificadoViewSet(viewsets.ModelViewSet):
    queryset = Certificado.objects.all()
    serializer_class = CertificadoSerializer
    authentication_classes = token
    permission_classes = permission


class CalibracaoViewSet(viewsets.ModelViewSet):
    queryset = Calibracao.objects.all()
    serializer_class = CalibracaoSerializer
    authentication_classes = token
    permission_classes = permission
