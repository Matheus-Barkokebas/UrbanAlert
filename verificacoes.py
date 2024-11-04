from empresa import *
from ocorrencia import *
import os

def verificar_empresa(cnpj, senha):
    dados_empresa = carregar_dados_emp()

    cnpj = cnpj.strip()
    senha = senha.strip()

    for empresa in dados_empresa:
        if str(empresa["cnpj"]) == cnpj and str(empresa["senha"]) == senha:
            return True
    return False