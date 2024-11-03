from flask import Flask, render_template, request

app = Flask(__name__)

class Pessoa:
    def __init__(self, nome, cpf, endereco):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco

    def __repr__(self):
        return f'Pessoa(nome={self.nome}, cpf={self.cpf}, endereco={self.endereco})'

class Profissao:
    def __init__(self, cod_profissao, profissao, status):
        self.cod_profissao = cod_profissao
        self.profissao = profissao
        self.status = status

    def __repr__(self):
        return f'Profissao(cod={self.cod_profissao}, profissao={self.profissao}, status={self.status})'

lista_de_pessoas = []
lista_de_profissoes = []

@app.route('/inicio')
def inicio():
    titulo = "Sistema de Gestão de Recursos Humanos (SGRH)"
    return render_template("lista2.html", pessoas=lista_de_pessoas, titulo=titulo)

@app.route('/form')
def form():
    titulo = "Cadastro de Pessoa"
    return render_template("form.html", titulo=titulo)

@app.route('/criar', methods=['POST'])
def criar():
    nome = request.form['nome']
    cpf = request.form['cpf']
    endereco = request.form['endereco']

    nova_pessoa = Pessoa(nome, cpf, endereco)
    lista_de_pessoas.append(nova_pessoa)

    return render_template("lista2.html", pessoas=lista_de_pessoas, titulo="Lista de Pessoas")

@app.route('/form_profissao')
def form_profissao():
    titulo = "Cadastro de Profissão"
    return render_template("form_profissao.html", titulo=titulo)

@app.route('/saida_profissao', methods=['POST'])
def saida_profissao():
    cod_profissao = request.form['cod_profissao']
    profissao = request.form['profissao']
    status = request.form['status']

    nova_profissao = Profissao(cod_profissao, profissao, status)
    lista_de_profissoes.append(nova_profissao)

    return render_template("saida_profissao.html", profissoes=lista_de_profissoes, titulo="Lista de Profissões")

if __name__ == '__main__':
    app.run()
