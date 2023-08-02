from clientes.models import Cliente
from clientes.validators import validator
from rest_framework import serializers


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        '''Valida os dados do cliente'''
        if not validator.cpf_valido(data['cpf']):
            raise serializers.ValidationError({"cpf": "O CPF deve conter 11 dígitos"})
        if not validator.nome_valido(data['nome']):
            raise serializers.ValidationError({"nome": "O nome deve conter apenas letras"})
        if not validator.rg_valido(data['rg']):
            raise serializers.ValidationError({"rg": "O rg deve conter 9 dígitos"})
        if not validator.celular_valido(data['celular']):
            raise serializers.ValidationError({"celular": "O celular deve seguir esse padrão: XX XXXX-XXXX"})
        

        return data
    
    
   
    
    