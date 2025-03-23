from flask import Flask
from flask_cors import CORS
from app.routes.usuarios import usuarios_bp
from app.routes.veiculos import veiculos_bp 
from app.routes.auth import auth_bp

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.register_blueprint(usuarios_bp, url_prefix="/api/usuarios")
    app.register_blueprint(veiculos_bp, url_prefix="/api/veiculos") 
    app.register_blueprint(auth_bp, url_prefix="/api/auth")

    return app
