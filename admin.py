import json
import os

arquivo_admin = "admin.json"

def carregar_dadosA():
    if os.path.exists (arquivo_admin):
        try: 
            with open (arquivo_admin , "r") as infile:
                return json.load(infile)
        except json.JSONDecodeError:
            print ("Erro ao ler o arquivo")
            return []
    return []

def salvar_dadosA(dados):
    with open (arquivo_admin , "w") as outfile:
        json.dump (dados, outfile, indent=4) 

def verificar_admin(id, senha):
    dados_admin = carregar_dadosA()

    id = id.strip()
    senha = senha.strip()

    for admin in dados_admin:
        if str(admin["id"]) == id and str(admin["senha"]) == senha:
            return True
    return False
