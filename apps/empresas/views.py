from apps.empresas.models import Empresa
from apps.empresas.serializers import EmpresaSerializer
from rest_framework import generics


class EmpresaListCreate(generics.ListCreateAPIView):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer