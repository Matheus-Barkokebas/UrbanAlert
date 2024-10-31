import json
import os

arquivo_ocorrencia = "ocorrencia.json"

def carregar_dados():
    if os.path.exists (arquivo_ocorrencia, "r"):
        try:
            with open (arquivo_ocorrencia, "r") as infile:
                return json.load (infile)
        except json.JSONDecodeError:
            print("Erro ao ler o arquivo.")
            return []
    return[] 

def salvar_dados(dados):
    with open (arquivo_ocorrencia, "w") as outfile:
        json.dump (dados, outfile, indent=4)

def criar_ocorrencia (qualOcorrencia, estadoOcorrencia, cidadeOcorrencia, bairroOcorrencia, ruaOcorrencia, horaOcorrencia, DetalhesOcorrencia, ):
    dados_ocorrencia = carregar_dados()

    nova_ocorrencia = {"qualOcorrencia": qualOcorrencia,
                       "estadoOcorrencia": estadoOcorrencia,
                       "cidadeOcorrencia": cidadeOcorrencia,
                       "bairroOcorrencia": bairroOcorrencia,
                       "ruaOcorrencia": ruaOcorrencia, 
                       "horaOcorrencia": horaOcorrencia,
                       "DetalhesOcorrencia": DetalhesOcorrencia}
    
    dados_ocorrencia.append(nova_ocorrencia)
    salvar_dados (dados_ocorrencia)
    print("ocorrencia salva com sucesso.")

def consultar_ocorrencia ():
    dados_ocorrencia = carregar_dados()

    if dados_ocorrencia:
        for ocorrencia in dados_ocorrencia:
            print(f"nome da ocorrencia {ocorrencia['qualOcorrencia']}")
            print(f"estado da ocorrencia {ocorrencia['estadoOcorrencia']}")
            print(f"cidade da ocorrencia {ocorrencia['cidadeOcorrencia']}")
            print(f"bairro da ocorrencia {ocorrencia['bairroOcorrencia']}")
            print(f"nome da rua {ocorrencia['ruaOcorrencia']}")
            print(f"hora da ocorrencia {ocorrencia['horaOcorrencia']}") 
            print(f"detalhe da ocorrencia {ocorrencia['detalheOcorrencia']}")
    else:
        print("Esses dados nao existem")

def atualitar_ocorrencia():
    dados_ocorrencia = carregar_dados()

    ocorrencia = input("Qual ocorrencia você quer atualizar?")
    ocorrencia_encontrada = False

    for i in dados_ocorrencia:
        if i["qualOcorrencia"] == ocorrencia:
            i['qualOcorrencia'] = print(f"Tipo de ocorrencia: {i['qualOcorrencia']}") or i['qualOcorrencia']
            i['estadoOcorrencia'] = print(f"Qual é o estado que aconteu?: {i['estadoOcorrencia']}") or i['estadoOcorrencia']
            i['cidadeOcorrencia'] = print(f"Qual é a cidade que aconteceu?: {i['cidadeOcorrencia']}") or i['cidadeOcorrencia']
            i['bairroOcorrencia'] = print(f"Qual é o bairro que aconteceu?: {i['bairroOconrrencia']}") or i['bairroOcorrencia']
            i['ruaOcorrencia'] = print(f"Qual é a rua que aconteceu?: {i['ruaOcorrencia']}") or i['ruaOcorrencia']
            i['horaOcorrencia'] = print(f"Que hora aconteceu?: {i['horaOcorrencia']}") or i['horaOcorrencia']
            i['detalheOcorrencia'] = print(f"Opsional: De mais detlhes sobre a ocorrencia : {i['detalheOcorrencia']}") or i['detalheOcorrencia']

            if ocorrencia_encontrada:
                salvar_dados(dados_ocorrencia)
                print("Ocorrencia atualizado!")
            
            else:
                print("Erro!")


def deletar_ocorrencia():
    dados_ocorrencia = carregar_dados()

    excluir_ocorrencia = print("Qual foi a ocorrencia?")
    lista_atualizada = [ocorrencia for ocorrencia in dados_ocorrencia if ocorrencia["ocorrencia"] != excluir_ocorrencia]

    if len (lista_atualizada) < len (lista_atualizada):
        salvar_dados (lista_atualizada)
        print(f"Ocorrencia {excluir_ocorrencia} excluido com sucesso!")
    else:
        print(f"Ocorrencia {excluir_ocorrencia} não encintrado")