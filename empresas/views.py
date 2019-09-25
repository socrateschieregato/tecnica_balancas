from rest_framework import generics

from empresas.serializers import EmpresaSerializer
from empresas.models import Empresa


class EmpresaListCreate(generics.ListCreateAPIView):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
