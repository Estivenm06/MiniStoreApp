# MiniStoreApp

# ES
Este projecto esta en fase de Desarrollo y el objetivo principal es un Gestor de Inventario de una Tienda Minorista la cual muestra la disponibilidad y el numero de productos disponible en el inventario en tiempo real.

# EN
This project it is in development phase and the main goal of this is the management of a story and shows here their stock and availability.

## Installation - Instalación

# ES
Primero se escribiran unos comandos para crear un ambiente virtual para instalar librerias de manera virtual con pip

# EN
Craete virtual Environment and install ministoreapp with pip

```bash
  python -m venv .venv
  # Use .venv as a folder or the name that you want
  source .venv/Scripts/activate
  # Once the Virtual Environment is created and initialized
  # Install flask
  pip install flask
```

## Running App - Inicializar Aplicación

# ES
Para inicializar la aplicación, ejeccuta los siguientes comandos
Ejecutalos desde el proyecto principal con

# EN
To run the app, run the following command
Run it from the project root with

```bash
    # Python
    python -m src.app
    # Flask
    flask --app app run --debug
```

# Project Structure -- Estructura del Proyecto

```
project_minstore/
├── package.json
├── README.md
└── src/
├── **init**.py # Flask application factory: create_app()
├── app.py # Application entry point
├── controllers/
│ ├── **init**.py
│ ├── clients_controller.py
│ ├── index_controller.py
│ ├── invoices_controller.py
│ ├── products_controller.py
│ └── reports_controller.py
├── js/
│ └── index.js
├── pages/
│ ├── error.html
│ ├── factura.html
│ ├── login.html
│ ├── menu.html
│ ├── productos.html
│ └── reportes.html
├── static/
│ └── css/
│ ├── brand.css
│ └── style.css
└── templates/
├── clientes/
│ └── clientes.html
├── facturacion/
│ └── facturacion.html
├── productos/
│ └── productos.html
├── reportes/
│ └── reportes.html
├── index.html
└── layout.html
```
