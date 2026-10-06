from flask import Blueprint, render_template

reports_bp = Blueprint('reportes', __name__)

@reports_bp.route('/reportes')
def reportes():
    return render_template('/reportes/reportes.html')