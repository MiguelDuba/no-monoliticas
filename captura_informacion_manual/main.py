from dotenv import load_dotenv
from flask import Flask, jsonify
from api.controller.house import house_api
from out.adapter.db.postgres import create_tables

loaded = load_dotenv('.env.development')

app = Flask(__name__)
app.register_blueprint(house_api)
create_tables()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3005)