from empresa import *
from ocorrencia import *
from verificacoes import *
from CRUDusuarios import *
import time
import os

PRETO = "\033[0;30m"
VERMELHO = "\033[0;31m"
VERDE = "\033[0;32m"
MARROM = "\033[0;33m"
AZUL = "\033[0;34m"
ROXO = "\033[0;35m"
CIANO = "\033[0;36m"
CINZA_CLARO = "\033[0;37m"
PRETO_CINZA = "\033[1;30m"
VERMELHO_CLARO = "\033[1;31m"
VERDE_CLARO = "\033[1;32m"
AMARELO = "\033[1;33m"
AZUL_CLARO = "\033[1;34m"
ROXO_CLARO = "\033[1;35m"
CIANO_CLARO = "\033[1;36m"
BRANCO_CLARO = "\033[1;37m"
BOLD = "\033[1m"
FAINT = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
BLINK = "\033[5m"
NEGATIVE = "\033[7m"
CROSSED = "\033[9m"
END = "\033[0m"
RESET = '\033[0m'
NEGRITO = '\033[1m'

while True:
    print(f"{AZUL}{"#"*30}") 
    print(f"{MARROM}{NEGRITO}|   1 - Entrar{RESET}")
    print(f"{MARROM}{NEGRITO}|   2 - Cadastrar{RESET}")
    print(f"{AZUL}{"#"*30}") 
    op_menu = int(input(f"{AMARELO}Escolha uma opcao: {RESET}"))
    
    match (op_menu):
        case 1:
            print(f"{AZUL}{NEGRITO}1 - Login usuario{RESET}")
            print(f"{AZUL}{NEGRITO}2 - Login empresa{RESET}")
            op_login = int(input(f"{AMARELO}Escolha uma opcao: {RESET}"))

            match (op_login):
                case 1:
                    cpf_input = input(f"{AMARELO}Digite seu CPF: {RESET}")
                    senha_input = input(f"{AMARELO}Digite sua senha: {RESET}")

                    if verificar_pessoa(cpf_input, senha_input):
                        print(f"{VERDE}Acesso concedido.{RESET}")
                        time.sleep(1)

                        print(f"{AMARELO}Validando informações...{RESET}")
                        time.sleep(1)

                    else:
                        print(f"{VERMELHO}Acesso negado.{RESET}")

                case 2:
                    cnpj_input = input(f"{AMARELO}Digite seu CNPJ: {RESET}")
                    senhaE_input = input(f"{AMARELO}Digite sua senha: {RESET}")

                    if verificar_empresa(cnpj_input, senhaE_input):
                        print(f"{AMARELO}Validando informações...{RESET}")
                        time.sleep(1)
                        print(f"{VERDE}Acesso concedido.{RESET}")
                    else:
                        print(f"{AMARELO}Validando informações...{RESET}")
                        time.sleep(1)
                        print(f"{VERMELHO}Acesso negado.{RESET}")
            
        case 2:
            print(f"{AZUL}{NEGRITO}1 - Usuario comum{RESET}")
            print(f"{AZUL}{NEGRITO}2 - Empresa{RESET}")
            op_cadastro = int(input(f"{AMARELO}Escolha uma opcao: {RESET}"))

            match (op_cadastro):
                case 1:
                    nome = input(f"{AMARELO}Informe seu nome: {RESET}")
                    idade = int(input(f"{AMARELO}Informe sua idade: {RESET}"))
                    cpf = int(input(f"{AMARELO}Informe seu CPF: {RESET}"))
                    email = input(f"{AMARELO}Informe seu email: {RESET}")
                    senha = input(f"{AMARELO}Informe sua senha: {RESET}")
                    telefone = int(input(f"{AMARELO}Informe seu telefone: {RESET}"))
                    endereco = input(f"{AMARELO}Informe seu endereço: {RESET}")
                    cidade = input(f"{AMARELO}Informe sua cidade: {RESET}")
                    estado = input(f"{AMARELO}Informe seu estado: {RESET}")
                    cep = int(input(f"{AMARELO}Informe seu CEP: {RESET}"))
                    
                    salvar_pessoaP(nome, idade, cpf, email, senha, telefone, endereco, cidade, estado, cep)

                    print(f"{AMARELO}Validando informações...{RESET}")
                    time.sleep(3)

                    print(f"{VERDE}Cadastro realizado com sucesso!{RESET}")

                case 2:
                    nome_empresa = input(f"{AMARELO}Informe o nome da empresa: {RESET}")
                    nome_pessoa_responsavel = input(f"{AMARELO}Informe o nome da pessoa responsável: {RESET}")
                    cnpj = input(f"{AMARELO}Informe o CNPJ da empresa: {RESET}")
                    telefoneDeContato = input(f"{AMARELO}Informe o telefone de contato da empresa: {RESET}")
                    endereco = input(f"{AMARELO}Informe o Endereco da empresa: {RESET}")
                    cidade = input(f"{AMARELO}Informe a cidade da empresa: {RESET}")
                    estado = input(f"{AMARELO}Informe o estado da empresa: {RESET}")
                    emailEmpresa = input(f"{AMARELO}Informe o email da empresa: {RESET}")
                    senhaEmpresa = input(f"{AMARELO}Informe a senha da empresa: {RESET}")

                    salvar_empresa (nome_empresa , nome_pessoa_responsavel , cnpj , telefoneDeContato , endereco , cidade , estado , emailEmpresa , senhaEmpresa)

                    print(f"{AMARELO}Validando informações...{RESET}")
                    time.sleep(3)

                    print(f"{VERDE}Cadastro realizado com sucesso!{RESET}")
