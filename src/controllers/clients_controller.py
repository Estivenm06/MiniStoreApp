from flask import Blueprint, render_template

clients_bp = Blueprint('clientes', __name__)

@clients_bp.route('/clientes')
def clientes():
    return render_template('/clientes/clientes.html')