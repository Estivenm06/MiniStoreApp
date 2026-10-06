# MiniStoreApp

This project it is in development phase and the main goal of this is the management of a story and shows here their stock and availability.

## Installation

Craete virtual Environment and install ministoreapp with pip

```bash
  python -m venv .venv
  # Use .venv as a folder or the name that you want
  source .venv/Scripts/activate
  # Once the Virtual Environment is created and initialized
  # Install flask
  pip install flask
```

## Running App

To run the app, run the following command

Run it from the project root with

```bash
    # Python
    python -m src.app
    # Flask
    flask --app app run --debug
```

# Project Structure

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
