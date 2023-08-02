import re
from validate_docbr import CPF


class validator:
    '''Classe para validar os dados do cliente'''
    @staticmethod
    def cpf_valido(Num_cpf):
        """Valida o tamnho do cpf"""
        cpf = CPF()
        return cpf.validate(Num_cpf)
    
    @staticmethod
    def nome_valido(nome):
        """Valida o nome"""
        return nome.isalpha()
    @staticmethod
    def rg_valido(rg):
        """Valida o rg"""    
        return len(rg)!=9 
    @staticmethod
    def celular_valido(celular):
        """Valida o numero do celular celular: XX XXXXX-XXXX (11 digitos)"""
        patter = '[0-9]{2} [0-9]{5}-[0-9]{4}'
        resposta = re.findall(patter, celular)
        return resposta
            