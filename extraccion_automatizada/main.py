from api.controller.companies import companies_blueprint
from flask import Flask
from out.adapter.db.postgres import create_tables

app = Flask(__name__)
app.register_blueprint(companies_blueprint)
create_tables()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)