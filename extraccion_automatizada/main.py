from modulos.companies.aplicacion.comandos.add_company_command import companies_blueprint
from flask import Flask

app = Flask(__name__)
app.register_blueprint(companies_blueprint)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)