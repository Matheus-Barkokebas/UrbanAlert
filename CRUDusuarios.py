# Classe para representar um usuário
class User:
    def __init__(self, nome, idade, cpf, email, senha, telefone, endereco, cidade, estado, cep):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.email = email
        self.senha = senha
        self.telefone = telefone
        self.endereco = endereco
        self.cidade = cidade
        self.estado = estado
        self.cep = cep

    def __str__(self):
        return (f"Nome: {self.nome}, Idade: {self.idade}, CPF: {self.cpf}, Email: {self.email}, "
                f"Telefone: {self.telefone}, Endereço: {self.endereco}, Cidade: {self.cidade}, "
                f"Estado: {self.estado}, CEP: {self.cep}")

# CRUD de usuários com uma lista
class UserCRUD:
    def __init__(self):
        self.users = []  # Lista para armazenar usuários

    def criar_usuario(self, nome, idade, cpf, email, senha, telefone, endereco, cidade, estado, cep):
        user = User(nome, idade, cpf, email, senha, telefone, endereco, cidade, estado, cep)
        self.users.append(user)
        print("Usuário cadastrado com sucesso!")

    def ler_usuario(self):
        if not self.users:
            print("Nenhum usuário cadastrado.")
        else:
            for user in self.users:
                print(user)

    def atualizar_usuario(self, cpf, **kwargs):
        for user in self.users:
            if user.cpf == cpf:
                for key, value in kwargs.items():
                    if value:
                        setattr(user, key, value)
                print("Usuário atualizado com sucesso!")
                return
        print("Usuário não encontrado.")

    def deletar_usuario(self, cpf, senha):
        for user in self.users:
            if user.cpf == cpf and user.senha == senha:
                self.users.remove(user)
                print("Usuário deletado com sucesso!")
                return
            else:
                print("CPF ou Senha incorreta(s)")
        print("Usuário não encontrado.")


# Menu para o CRUD de usuários
def menu():
    crud = UserCRUD()

    while True:
        print("\n1. Cadastrar novo usuário")
        print("2. Listar usuários")
        print("3. Atualizar usuário")
        print("4. Deletar usuário")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            nome = input("Digite o nome: ")
            idade = input("Digite a idade: ")
            cpf = input("Digite o CPF: ")
            email = input("Digite o email: ")
            senha = input("Digite a senha: ")
            telefone = input("Digite o telefone: ")
            endereco = input("Digite o endereço: ")
            cidade = input("Digite a cidade: ")
            estado = input("Digite o estado: ")
            cep = input("Digite o CEP: ")
            crud.criar_usuario(nome, idade, cpf, email, senha, telefone, endereco, cidade, estado, cep)

        elif opcao == "2":
            crud.ler_usuario()

        elif opcao == "3":
            cpf = input("Digite o CPF do usuário a ser atualizado: ")
            updates = {}
            fields = ["nome", "idade", "cpf", "email", "senha", "telefone", "endereco", "cidade", "estado", "cep"]
            for field in fields:
                value = input(f"Novo {field} (ou pressione Enter para manter): ")
                updates[field] = value if value else None
            crud.atualizar_usuario(cpf, **updates)

        elif opcao == "4":
            cpf = input("Digite o CPF do usuário a ser deletado: ")
            senha = input("Digite a senha do usuário a ser deletado: ")
            crud.deletar_usuario(cpf, senha)
             

        elif opcao == "5":
            print("Saindo do sistema.")
            break

        else:
            print("Opção inválida, tente novamente.")

menu()
