from flask import Blueprint, render_template, request
from database.cliente import CLIENTES

cliente_route = Blueprint('cliente', __name__)


@cliente_route.route('/')  # /clientes/
def lista_clientes():
    """Listar os clientes"""
    return render_template('lista_clientes.html', clientes=CLIENTES)


@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    """Inserir os dados do cliente"""
    data = request.json
    novo_usuario = {
        "id":len(CLIENTES)+1,
        "nome": data['nome'],
        "email":data['email'],
    }
    CLIENTES.append(novo_usuario)
    return render_template('item_cliente.html', cliente=novo_usuario)


@cliente_route.route('/new')
def form_cliente():
    """ Formulário para cadastrar um cliente """
    return render_template('form_cliente.html')


@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
    """ Exibir detalhes de um cliente """

    cliente = list(filter(lambda c: c['id'] == cliente_id, CLIENTES))[0]
    return render_template('detalhe_cliente.html', cliente=cliente)


@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
    """ Formulario para editar um cliente """
    cliente = None
    for c in CLIENTES:
        if c['id'] == cliente_id:
            cliente = c
    return render_template('form_cliente.html', cliente=cliente)


@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def atualizar_cliente(cliente_id):
    """ Atualizar informações de um cliente """
    cliente_editado = None

    # Obter dados do form de edição
    data = request.json

    # Obter usuário pelo id
    for c in CLIENTES:
        if c['id'] == cliente_id:
            c['nome'] = data['nome']
            c['email'] = data['email']

            cliente_editado = c

    # Editar usuário
    return render_template('item_cliente.html', cliente=cliente_editado)


@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def deletar_cliente(cliente_id):
    """ Deletar informações de um cliente """
    global CLIENTES
    CLIENTES = [ c for c in CLIENTES if c['id'] != cliente_id]
    return {'deleted': 'ok'}
