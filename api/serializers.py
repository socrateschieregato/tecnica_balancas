from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from calibracoes.models import Peso, Certificado, Calibracao
from empresas.models import Empresa
from equipamentos.models import Equipamento


class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user


class EquipamentoSerializer(serializers.ModelSerializer):
    empresa = serializers.SlugRelatedField(many=False, read_only=True, slug_field='nome_razao')
    tipo = serializers.SlugRelatedField(many=False, read_only=True, slug_field='descricao')
    desvio = serializers.SlugRelatedField(many=False, read_only=True, slug_field='valor')
    usuario = serializers.SlugRelatedField(many=False, read_only=True, slug_field='username')

    class Meta:
        model = Equipamento
        fields = '__all__'


class PesoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Peso
        fields = '__all__'


class CertificadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificado
        fields = '__all__'


class CalibracaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calibracao
        fields = '__all__'
