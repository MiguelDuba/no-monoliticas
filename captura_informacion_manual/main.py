from flask import Flask, jsonify
from modulos.office_report.aplicacion.comandos.office_report_create import office_report_api
from config.db import create_tables

app = Flask(__name__)
app.register_blueprint(office_report_api)
create_tables()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3005)