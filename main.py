from flask import Flask, url_for, render_template

# Inicialização
app = Flask(__name__)  # Forma de inicializar o flask, name serve para identificar e organizar os recursos do projeto


# Rotas
@app.route('/', methods=['GET']) # Por padrão já tem o get
def ola_mundo():
    titulo = "Gestão de usuários"
    usuarios = [
        {"nome": "Thiago", "membro_ativo": True},
        {"nome": "Felipe", "membro_ativo": False},
        {"nome": "Juliana", "membro_ativo": False},
    ]
    # render_template serve para importar os arquivos dentro da pasta templates
    return render_template("index.html", titulo=titulo, usuarios=usuarios)


@app.route('/sobre', methods=['GET']) # Por padrão já tem o get
def pagina_sobre():
    return """
        <b>Pesquisa google</b>
        <a href="https://google.com">Google</a>
    """


# Função responsável por executar o nosso servidor web (Execução)
app.run(debug=True)  # Debug serve para identificar para o Flask que estamos no modo desenvolvedor
