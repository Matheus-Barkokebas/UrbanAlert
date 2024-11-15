from flask import Flask, render_template, redirect, request, session, url_for, flash
from pessoa import *
from empresa import *
from ocorrencia import *
from admin import *

import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SENHA'

arquivo_pessoa = "pessoa.json"
arquivo_ocorrencia = "ocorrencia.json"
arquivo_empresa = "empresa.json"

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/logar', methods=['POST'])
def logar():
    cpfCnpj = request.form.get('cpfCnpj')
    senha = request.form.get('senha')

    logado = verificar_pessoa(cpfCnpj, senha)
    logado2 = verificar_empresa(cpfCnpj, senha)
    adminLogados = verificar_admin(cpfCnpj, senha)

    if logado or logado2:
        session['cpfCnpj'] = cpfCnpj
        return render_template('site.html')
    elif adminLogados:
        session['cpfCnpj'] = cpfCnpj
        return render_template('admin.html')
    else:
        flash('CPF/CNPJ ou Senha invalidos')
        return render_template('login.html')

@app.route('/cadastresse')
def cadastresse():
    return render_template('menuCadastro.html')

@app.route('/menuCadastroP')
def menuPessoa():
    return render_template('cadastro.html')

@app.route('/menuCadastroE')
def menuEmpresa():
    return render_template('cadastroEmpresa.html')

@app.route('/cadastrarPessoa', methods=['POST'])
def cadastrar():
    nome = request.form.get('nome')
    idade = request.form.get('idade')
    cpf = request.form.get('cpf')
    email = request.form.get('email')
    senha = request.form.get('senha')
    telefone = request.form.get('telefone')
    endereco = request.form.get('endereco')
    cidade = request.form.get('cidade')
    estado = request.form.get('estado')
    cep = request.form.get('cep')

    salvar_pessoaP(nome, idade, cpf, email, senha, telefone, endereco, cidade, estado, cep)
    return render_template('login.html')

@app.route('/cadastroEmpresa', methods=['POST'])
def empresa():
    nomeEmpresa = request.form.get('nomeEmpresa')
    responsavelEmpresa = request.form.get('responsavelEmpresa')
    cnpj = request.form.get('cnpj')
    telefoneEmpresa = request.form.get('telefoneEmpresa')
    enderecoEmpresa = request.form.get('enderecoEmpresa')
    cidadeEmpresa = request.form.get('cidadeEmpresa')
    estadoEmpresa = request.form.get('estadoEmpresa')
    emailEmpresa = request.form.get('emailEmpresa')
    senhaEmpresa = request.form.get('senhaEmpresa')

    salvar_empresa(nomeEmpresa, responsavelEmpresa, cnpj, telefoneEmpresa, enderecoEmpresa, cidadeEmpresa, estadoEmpresa, emailEmpresa, senhaEmpresa)
    return render_template('login.html')

@app.route('/voltarSite')
def nomeSite():
    return render_template('site.html')

@app.route('/bntComecar')
def bntComecar():
    return render_template('criarOcorrencia.html')

@app.route('/criarOcorrencia')
def criarOcorrencia():
    return render_template('criarOcorrencia.html')

@app.route('/cadastrarOcorrencia', methods=['POST'])
def cadastrarOcorrencia():
    nomeOcorrencia = request.form.get('nomeOcorrencia')
    estadoOcorrencia = request.form.get('estadoOcorrencia')
    cidadeOcorrencia = request.form.get('cidadeOcorrencia')
    bairroOcorrencia = request.form.get('bairroOcorrencia')
    ruaOcorrencia = request.form.get('ruaOcorrencia')
    horaOcorrencia = request.form.get('horaOcorrencia')
    DetalhesOcorrencia = request.form.get('DetalhesOcorrencia')

    criar_ocorrencia (nomeOcorrencia, estadoOcorrencia, cidadeOcorrencia, bairroOcorrencia, ruaOcorrencia, horaOcorrencia, DetalhesOcorrencia)
    return render_template('criarOcorrencia.html')

@app.route('/listarOcorrencia')
def listarOcorrencia():
    with open(arquivo_ocorrencia, "r") as outfile:
        dadosOcorrencia = json.load(outfile)
    return render_template('listarOcorrencia.html', dadosOcorrencia=dadosOcorrencia)

@app.route('/voltar')
def voltar():
    return render_template('login.html')

@app.route('/verPerfil')
def verPerfil():
    cpfCnpj = session.get('cpfCnpj')
    if not cpfCnpj:
        return redirect(url_for('home'))

    with open(arquivo_pessoa, "r") as infile:
        usuarios = json.load(infile)
        usuario_logado = next((u for u in usuarios if u["cpf"] == cpfCnpj), None)
    with open(arquivo_empresa, "r") as infile:
        empresa = json.load(infile)
        empresa_logada = next((e for e in empresa if e["cnpj"] == cpfCnpj), None)

    if usuario_logado or empresa_logada:
        return render_template('perfil.html', usuario=usuario_logado, empresa=empresa_logada)
    
    else:
        return redirect(url_for('home'))
    
@app.route('/atualizarConta')
def atualizarConta():
    cpfCnpj = session.get('cpfCnpj')
    if not cpfCnpj:
        return redirect(url_for('home'))

    with open(arquivo_pessoa, "r") as infile:
        usuarios = json.load(infile)
        usuario_logado = next((u for u in usuarios if u["cpf"] == cpfCnpj), None)
    with open(arquivo_empresa, "r") as infile:
        empresa = json.load(infile)
        empresa_logada = next((e for e in empresa if e["cnpj"] == cpfCnpj), None)

    if usuario_logado:
        return render_template('atualizar.html', usuario=usuario_logado)
    elif empresa_logada:
        return render_template('atualizar.html', empresa=empresa_logada)
    else:
        return redirect(url_for('home'))

@app.route('/atualizar', methods=['POST'])
def atualizarPessoa():
    with open(arquivo_pessoa, "r") as infile:
        lista_pessoa = json.load(infile)

    cpfCnpj = session.get('cpfCnpj')
    pessoa_encontrada = False

    for usuario in lista_pessoa:
        if usuario["cpf"] == cpfCnpj:
            pessoa_encontrada = True
            
            usuario['nome'] = request.form.get('atualizarNome') or usuario['nome']
            usuario['idade'] = request.form.get('atualizarIdade') or usuario['idade']
            usuario['email'] = request.form.get('atualizarEmail') or usuario['email']
            usuario['senha'] = request.form.get('atualizarSenha') or usuario['senha']
            usuario['telefone'] = request.form.get('atualizarTelefone') or usuario['telefone']
            usuario['endereco'] = request.form.get('atualizarEndereco') or usuario['endereco']
            usuario['cidade'] = request.form.get('atualizarCidade') or usuario['cidade']
            usuario['estado'] = request.form.get('atualizarEstado') or usuario['estado']
            usuario['cep'] = request.form.get('atualizarCep') or usuario['cep']
            break

    if pessoa_encontrada:
        with open(arquivo_pessoa, "w") as outfile:
            json.dump(lista_pessoa, outfile, indent=4)
        print("Dados atualizados com sucesso.")
        return render_template('site.html')
    else:
        print("Pessoa com esse CPF não foi encontrada.")

@app.route('/atualizarEmpresa', methods=['POST'])
def atualizarEmpresa():
    with open(arquivo_empresa, "r") as infile:
        lista_empresas = json.load(infile)

    cpfCnpj = session.get('cpfCnpj')
    empresa_encontrada = False

    for empresa in lista_empresas:
        if empresa["cnpj"] == cpfCnpj:
            empresa_encontrada = True

            empresa ['nomeEmpresa'] = request.form.get('nomeEmpresa') or empresa ['nomeEmpresa']
            empresa ['responsavelEmpresa'] = request.form.get('responsavelEmpresa') or empresa ['responsavelEmpresa']
            empresa ['cnpj'] = request.form.get('cnpj') or empresa ['cnpj']
            empresa ['telefone'] = request.form.get('telefoneEmpresa') or empresa ['telefone']
            empresa ['endereco'] = request.form.get('enderecoEmpresa') or empresa ['endereco']
            empresa ['cidade'] = request.form.get('cidadeEmpresa') or empresa ['cidade']
            empresa ['estado'] = request.form.get('estadoEmpresa') or empresa ['estado']
            empresa ['email'] = request.form.get('emailEmpresa') or empresa ['email']
            empresa ['senha'] = request.form.get('senhaEmpresa') or empresa ['senha']
            break

    if empresa_encontrada:
        with open(arquivo_empresa, "w") as outfile:
            json.dump(lista_empresas, outfile, indent=4)
        return render_template('site.html')
    else:
        return False

@app.route('/deletarConta')
def deletarPerfil():
    cpfCnpj = session.get('cpfCnpj')
    
    with open(arquivo_pessoa, "r") as infile:
        usuarios = json.load(infile)
    
    lista_atualizada_pessoas = [u for u in usuarios if u["cpf"] != cpfCnpj]

    if len(lista_atualizada_pessoas) < len(usuarios):
        with open(arquivo_pessoa, "w") as outfile:
            json.dump(lista_atualizada_pessoas, outfile, indent=4)  
        session.pop('cpfCnpj', None)
        return redirect(url_for('home'))
    
    with open(arquivo_empresa, "r") as infile:
        empresas = json.load(infile)

    lista_atualizada_empresas = [e for e in empresas if e["cnpj"] != cpfCnpj]

    if len(lista_atualizada_empresas) < len(empresas):
        with open(arquivo_empresa, "w") as outfile:
            json.dump(lista_atualizada_empresas, outfile)
        session.pop('cpfCnpj', None)
        return redirect(url_for('home'))
    
    return render_template('perfil.html')

@app.route('/criarPessoaAdmin')
def criarPessoaAdmin():
    return render_template('criarPadmin.html')

@app.route('/cadastrarPessoaAdmin', methods=['POST'])
def cadastrarPessoaAdmin():
    nome = request.form.get('nomeAdmin')
    idade = request.form.get('idadeAdmin')
    cpf = request.form.get('cpfAdmin')
    email = request.form.get('emailAdmin')
    senha = request.form.get('senhaAdmin')
    telefone = request.form.get('telefoneAdmin')
    endereco = request.form.get('enderecoAdmin')
    cidade = request.form.get('cidadeAdmin')
    estado = request.form.get('estadoAdmin')
    cep = request.form.get('cepAdmin')

    salvar_pessoaP(nome, idade, cpf, email, senha, telefone, endereco, cidade, estado, cep)
    return render_template('admin.html')

@app.route('/criarEmpresaAdmin')
def criarEmpresaAdmin():
    return render_template('criarEadmin.html')

@app.route('/cadastroEmpresaAdmin', methods=['POST'])
def empresaAdmin():
    nomeEmpresa = request.form.get('nomeEmpresaAdmin')
    responsavelEmpresa = request.form.get('responsavelEmpresaAdmin')
    cnpj = request.form.get('cnpjAdmin')
    telefoneEmpresa = request.form.get('telefoneEmpresaAdmin')
    enderecoEmpresa = request.form.get('enderecoEmpresaAdmin')
    cidadeEmpresa = request.form.get('cidadeEmpresaAdmin')
    estadoEmpresa = request.form.get('estadoEmpresaAdmin')
    emailEmpresa = request.form.get('emailEmpresaAdmin')
    senhaEmpresa = request.form.get('senhaEmpresaAdmin')

    salvar_empresa(nomeEmpresa, responsavelEmpresa, cnpj, telefoneEmpresa, enderecoEmpresa, cidadeEmpresa, estadoEmpresa, emailEmpresa, senhaEmpresa)
    return render_template('admin.html')

@app.route('/voltarAdmin')
def voltarAdmin():
    return render_template('admin.html')

@app.route('/ocorrenciaAdmin')
def ocorrenciaAdmin():
    return render_template('ocorrenciaAdmin.html')

@app.route('/listarOcorreAdmin')
def listarOcorreAdmin():
    with open(arquivo_ocorrencia, "r") as outfile:
        dadosOcorrencia = json.load(outfile)
    return render_template('visuOcorrAdmin.html', dadosOcorrencia=dadosOcorrencia)

@app.route('/listarPessoaAdmin')
def listarPessoaAdmin():
    with open(arquivo_pessoa, "r") as outfile:
        dadosPessoa = json.load(outfile)
    return render_template('visuUsuarioAdm.html', dadosPessoa=dadosPessoa)

@app.route('/listarEmpresaAdmin')
def listarEmpresaAdmin():
    with open(arquivo_empresa, "r") as outfile:
        dadosEmpresa = json.load(outfile)
    return render_template('visuEmpAdm.html', dadosEmpresa=dadosEmpresa)

@app.route('/sair')
def sair():
    session.pop('cpf', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
