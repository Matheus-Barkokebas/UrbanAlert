import json 
import os

arquivo_empresa = "empresa.json"


def carregar_dados():
    if os.path.exists (arquivo_empresa):
        try: 
            with open (arquivo_empresa , "r") as infile:
                return json.load (infile)
        except json.JSONDecodeError:
            print ("Erro ao ler o arquivo")
            return []
    return []


def salvar_dados(dados):
    with open (arquivo_empresa , "w") as outfile:
        json.dump (dados, outfile, indent=4) 


def salvar_empresa (nomeEmpresa , responsavelEmpresa , cnpj , telefone , endereco , cidade , estado , email , senha):
    dados_empresa = carregar_dados()

    nova_empresa = {
        "nomeEmpresa" : nomeEmpresa,
        "responsavelEmpresa" : responsavelEmpresa,
        "cnpj" : cnpj,
        "telefone" : telefone,
        "endereco" : endereco,
        "cidade" : cidade,
        "estado" : estado,
        "email" : email,
        "senha" : senha}
    
    dados_empresa.append (nova_empresa)
    salvar_dados (dados_empresa)
    print ("Empresa salva com sucesso!")


def consultar_empresa ():
    dados_empresa = carregar_dados()

    if dados_empresa:
        for empresa in dados_empresa:
            print (f"\nNome da empresa: {empresa['nomeEmpresa']}")
            print (f"\nResponsavel da empresa: {empresa['responsavelEmpresa']}")
            print (f"\nCNPJ da empresa: {empresa['cnpj']}")
            print (f"\nTelefone da empresa: {empresa['telefone']}")
            print (f"\nEndereco da empresa: {empresa['endereco']}")
            print (f"\nCidade da empresa: {empresa['cidade']}")
            print (f"\nEstado da empresa: {empresa['estado']}")
            print (f"\nEmail da empresa: {empresa['email']}")
            print (f"\nSenha da empresa: {empresa['senha']}")
    
    else: 
        print ("Sem cadastro")

    
def atualizar_empresa ():
    dados_empresa = carregar_dados()

    cnpj_empresa = int(input("Qual o cnpj que deseja atualoizar? "))
    empresa_encontrada = False

    for empresa in dados_empresa:
        if empresa["cnpj"] == cnpj_empresa:
            empresa_encontrada = True
            print ("Atualizando dados (Deixe em branco caso queira manter o dado atual)")

            empresa ['nomeEmpresa'] = input (f"Novo nome[{empresa['nomeEmpresa']}]:") or empresa ['nomeEmpresa']
            empresa ['responsavelEmpresa'] = input (f"Novo responsavel[{empresa['responsavelEmpresa']}]:") or empresa ['responsavelEmpresa']
            empresa ['cnpj'] = input (f"Novo cnpj[{empresa['cnpj']}]:") or empresa ['cnpj']
            empresa ['telefone'] = input (f"Novo telefone[{empresa['telefone']}]:") or empresa ['telefone']
            empresa ['endereco'] = input (f"Novo endereco[{empresa['endereco']}]:") or empresa ['endereco']
            empresa ['cidade'] = input (f"Nova cidade[{empresa['cidade']}]:") or empresa ['cidade']
            empresa ['estado'] = input (f"Novo estado[{empresa['estado']}]:") or empresa ['estado']
            empresa ['email'] = input (f"Novo email[{empresa['email']}]:") or empresa ['email']
            empresa ['senha'] = input (f"Nova senha[{empresa['senha']}]:") or empresa ['senha']

            if empresa_encontrada:
                salvar_dados (dados_empresa)
                print ("Dados foram atualizados!")

            else:
                print ("Erro!")

        
def excluir_empresa ():
    dados_empresa = carregar_dados ()
    
    cnpj_excluir = input ("Qual CNPJ da empresa?")
    lista_atualizada = [empresa for empresa in dados_empresa if empresa["cnpj"] != cnpj_excluir]

    if len (lista_atualizada) < len (dados_empresa):
        salvar_dados (lista_atualizada)
        print (f"CNPJ {cnpj_excluir} excluido com sucesso!")

    else:
        print (f"CNPJ {cnpj_excluir} nao encontrado")


def menu ():
    print ("1-Cadastrar \n2-Consultar \n3-Atualizar \n4-Deletar")
    op = int (input("Escolha uma opcao: "))
    
    match (op):
        case 1: 
            nomeEmpresa = (input("Digite o nome da empresa: "))
            responsavelEmpresa = (input("Digite o nome do responsavel da empresa: "))
            cnpj = int(input("Digite o cnpj da empresa: "))
            telefone = int(input("Digite o telefone da empresa: "))
            endereco = (input("Digite o endereco da empresa: "))
            cidade = (input("Digite a cidade da empresa: "))
            estado = (input("Digite o estado da empresa: "))
            email = (input("Digite o email da empresa: "))
            senha = (input("Digite a senha da empresa: "))

            salvar_empresa (nomeEmpresa , responsavelEmpresa , cnpj , telefone , endereco , cidade , estado , email , senha)

        case 2:
            consultar_empresa()
        
        case 3: 
            atualizar_empresa()

        case 4: 
            excluir_empresa ()

menu()