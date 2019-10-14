from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from api.serializers import (
    EmpresaSerializer,
    UserSerializer,
    EquipamentoSerializer,
    TipoEquipamentoSerializer, UnidadeSerializer, DesvioSerializer)
from empresas.models import Empresa
from equipamentos.models import Equipamento, Tipo_equipamento
from tabelas.models import Unidade, Desvio

token = (TokenAuthentication, )
permission = (IsAuthenticated, )

class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    authentication_classes = token
    permission_classes = permission


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
    

class TipoEquipamentoViewSet(viewsets.ModelViewSet):
    queryset = Tipo_equipamento.objects.all()
    serializer_class = TipoEquipamentoSerializer
    authentication_classes = token
    permission_classes = permission


class UnidadeViewSet(viewsets.ModelViewSet):
    queryset = Unidade.objects.all()
    serializer_class = UnidadeSerializer
    authentication_classes = token
    permission_classes = permission


class DesvioViewSet(viewsets.ModelViewSet):
    queryset = Desvio.objects.all()
    serializer_class = DesvioSerializer
    authentication_classes = token
    permission_classes = permission


