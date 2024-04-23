from flask import Flask
from routes.home import home_route
from routes.cliente import cliente_route

# Inicialização
app = Flask(__name__)  # Forma de inicializar o flask, name serve para identificar e organizar os recursos do projeto

app.register_blueprint(home_route)
app.register_blueprint(cliente_route, url_prefix='/clientes')

# Função responsável por executar o nosso servidor web (Execução)
app.run(debug=True)  # Debug serve para identificar para o Flask que estamos no modo desenvolvedor
