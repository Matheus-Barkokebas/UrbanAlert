# UrbanAlert
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