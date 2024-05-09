from flask import Flask
from configuration import configure_all

# Inicialização
app = Flask(__name__)  # Forma de inicializar o flask, name serve para identificar e organizar os recursos do projeto

configure_all(app)

# Função responsável por executar o nosso servidor web (Execução)
app.run(debug=True)  # Debug serve para identificar para o Flask que estamos no modo desenvolvedor
