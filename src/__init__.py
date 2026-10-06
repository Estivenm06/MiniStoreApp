from flask import Flask

def create_app():
    app = Flask(__name__)

    from src.controllers.index_controller import index_bp
    from src.controllers.clients_controller import clients_bp
    from src.controllers.reports_controller import reports_bp
    from src.controllers.invoices_controller import invoices_bp
    from src.controllers.products_controller import products_bp

    app.register_blueprint(index_bp)
    app.register_blueprint(clients_bp)
    app.register_blueprint(reports_bp)
    app.register_blueprint(invoices_bp)
    app.register_blueprint(products_bp)

    return app
