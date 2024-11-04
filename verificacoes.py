from empresa import *
from ocorrencia import *
from CRUDusuarios import *
import os

def verificar_empresa(cnpj, senha):
    dados_empresa = carregar_dados_emp()

    cnpj = cnpj.strip()
    senha = senha.strip()

    for empresa in dados_empresa:
        if str(empresa["cnpj"]) == cnpj and str(empresa["senha"]) == senha:
            return True
    return False

def verificar_pessoa(cpf, senha):
    dados_pessoa = carregar_dadosP()

    cpf = cpf.strip()
    senha = senha.strip()

    for pessoa in dados_pessoa:
        if str(pessoa["cpf"]) == cpf and str(pessoa["senha"]) == senha:
            print(f"Login bem-sucedido! Bem-vindo(a), {pessoa['nome']}.")
            return True

    print("CPF ou senha incorretos.")
    return False