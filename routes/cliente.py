from flask import Blueprint

cliente_route = Blueprint('cliente', __name__)


@cliente_route.route('/')  # /clientes/
def lista_clientes():
    """Listar os clientes"""
    return render_template('lista_clientes.html')


@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    """Inserir os dados do cliente"""
    pass


@cliente_route.route('/new')
def form_cliente():
    """ Formulário para cadastrar um cliente """
    return {'pagina': "formulario clientes"}


@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
    """ Exibir detalhes de um cliente """
    pass


@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
    """ Formulario para editar um cliente """
    pass


@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def atualizar_cliente(cliente_id):
    """ Atualizar informações de um cliente """
    pass


@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def deletar_cliente(cliente_id):
    """ Deletar informações de um cliente """
    pass
