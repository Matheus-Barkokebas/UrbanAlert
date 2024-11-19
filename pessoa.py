import json
import os
from flask import Flask, render_template, redirect, request, session, url_for, flash

arquivo_pessoa = "pessoa.json"

def carregar_dadosP():
    if os.path.exists(arquivo_pessoa):
        try:
            with open(arquivo_pessoa, "r") as infile:
                return json.load(infile)
        except json.JSONDecodeError:
            print("Erro ao ler o arquivo JSON.")
            return []
    return []

def salvar_dados(dados):
    with open(arquivo_pessoa, "w") as outfile:
        json.dump(dados, outfile, indent=4)

def salvar_pessoaP(nome, idade, cpf, email, senha, telefone, endereco, cidade, estado, cep):
    dados_pessoa = carregar_dadosP()    
    
    for pessoa in dados_pessoa:
        if pessoa["cpf"] == cpf:
            flash('CPF ja cadastrado')
            return False
    
    nova_pessoa = {
        "nome": nome,
        "idade": idade,
        "cpf": cpf,
        "email": email,
        "senha": senha,
        "telefone": telefone,
        "endereco": endereco,
        "cidade": cidade,
        "estado": estado,
        "cep": cep,}
    
    dados_pessoa.append(nova_pessoa)
    salvar_dados(dados_pessoa)
    return True

def consultar_pessoas():
    dados_pessoa = carregar_dadosP()
    
    if dados_pessoa:
        for pessoa in dados_pessoa:
            print(f"\nNome: {pessoa['nome']}")
            print(f"Idade: {pessoa['idade']}")
            print(f"CPF: {pessoa['cpf']}")
            print(f"Email: {pessoa['email']}")
            print(f"Telefone: {pessoa['telefone']}")
            print(f"Endereço: {pessoa['endereco']}, {pessoa['cidade']}, {pessoa['estado']} - {pessoa['cep']}")
    else:
        print("Nenhuma pessoa encontrada.")
    
def atualizar_pessoa():
    dados_pessoa = carregar_dadosP()
    
    cpf_atualizar = input("Digite o CPF da pessoa a ser atualizada: ")
    pessoa_encontrada = False
    
    for pessoa in dados_pessoa:
        if pessoa["cpf"] == cpf_atualizar:
            pessoa_encontrada = True
            print("Atualizando dados (deixe em branco para manter o valor atual):")
            
            pessoa['nome'] = input(f"Novo nome [{pessoa['nome']}]: ") or pessoa['nome']
            pessoa['idade'] = input(f"Nova idade [{pessoa['idade']}]: ") or pessoa['idade']
            pessoa['email'] = input(f"Novo email [{pessoa['email']}]: ") or pessoa['email']
            pessoa['senha'] = input(f"Nova senha [{pessoa['senha']}]: ") or pessoa['senha']
            pessoa['telefone'] = input(f"Novo telefone [{pessoa['telefone']}]: ") or pessoa['telefone']
            pessoa['endereco'] = input(f"Novo endereço [{pessoa['endereco']}]: ") or pessoa['endereco']
            pessoa['cidade'] = input(f"Nova cidade [{pessoa['cidade']}]: ") or pessoa['cidade']
            pessoa['estado'] = input(f"Novo estado [{pessoa['estado']}]: ") or pessoa['estado']
            pessoa['cep'] = input(f"Novo CEP [{pessoa['cep']}]: ") or pessoa['cep']
            break
    
    if pessoa_encontrada:
        salvar_dados(dados_pessoa)
        print("Dados atualizados com sucesso.")
    else:
        print("Pessoa com esse CPF não foi encontrada.")

def excluir_pessoa():
    dados_pessoa = carregar_dadosP()
    
    cpf_excluir = input("Digite o CPF da pessoa a ser excluída: ")
    lista_atualizada = [pessoa for pessoa in dados_pessoa if pessoa["cpf"] != cpf_excluir]
    
    if len(lista_atualizada) < len(dados_pessoa):
        salvar_dados(lista_atualizada)
        print(f"Pessoa com CPF {cpf_excluir} excluída com sucesso.")    
    else:
        print(f"Pessoa com CPF {cpf_excluir} não encontrada.")

def listar_empresa_por_cnpj():
    dados_pessoa = carregar_dadosP()
    
    if not dados_pessoa:
        print("Nenhuma pessoa cadastrada.")
        return

    cpf_a_buscar = input("Por questoes de seguranca, digite seu CPF: ")
    
    for pessoa in dados_pessoa:
        if str(pessoa["cpf"]) == cpf_a_buscar:
            print(f"\nNome: {pessoa['nome']}")
            print(f"Idade: {pessoa['idade']}")
            print(f"CPF: {pessoa['cpf']}")
            print(f"Email: {pessoa['email']}")
            print(f"Telefone: {pessoa['telefone']}")
            print(f"Endereço: {pessoa['endereco']}, {pessoa['cidade']}, {pessoa['estado']} - {pessoa['cep']}")
            return
    
    print(f"Pessoa com CPF {cpf_a_buscar} não encontrada.")

def verificar_pessoa(cpf, senha):
    dados_pessoa = carregar_dadosP()

    cpf = cpf.strip()
    senha = senha.strip()

    for pessoa in dados_pessoa:
        if str(pessoa["cpf"]) == cpf and str(pessoa["senha"]) == senha:
            return True
    return False