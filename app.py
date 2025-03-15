from flask import Flask, send_from_directory
from config import db, migrate
from dotenv import load_dotenv
import os
from routes.user import user_bp
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from flask_jwt_extended import JWTManager

load_dotenv()

app = Flask(__name__)
CORS(app)
app.config['JWT_SECRET_KEY']= 'cada lobo tiene a su loba auuuuuuuu'
jwt = JWTManager(app) 


app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate.init_app(app, db)

app.register_blueprint(user_bp, url_prefix="/users")

# Configuración de Swagger UI
SWAGGER_URL = "/docs"  # URL donde se servirá la documentación
API_URL = "/swagger.yaml"  # Ruta donde se encuentra el archivo YAML

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL, API_URL, config={"app_name": "API de Usuarios"}
)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

# Servir el archivo YAML de forma estática
@app.route("/swagger.yaml")
def send_swagger():
    return send_from_directory(os.getcwd(), "swagger.yaml")

if __name__ == "__main__":
    app.run(debug=True)
