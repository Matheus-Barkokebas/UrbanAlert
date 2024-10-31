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
    

    

    
    

