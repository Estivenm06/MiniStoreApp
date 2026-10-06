from flask import Blueprint, render_template

products_bp = Blueprint('productos', __name__)

@products_bp.route('/productos')
def productos():
    return render_template('/productos/productos.html')