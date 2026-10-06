from flask import Blueprint, render_template

invoices_bp = Blueprint('facturacion', __name__)

@invoices_bp.route('/facturacion')
def facturacion():
    return render_template('/facturacion/facturacion.html')