from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from empresas.models import Empresa
from equipamentos.models import Equipamento, Tipo_equipamento
from tabelas.models import Unidade, Desvio


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
    class Meta:
        model = Equipamento
        fields = '__all__'


class TipoEquipamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_equipamento
        fields = '__all__'


class UnidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unidade
        fields = '__all__'


class DesvioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Desvio
        fields = '__all__'
