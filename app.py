from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
import os

# ====== RUTA DB ======
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, "pfo2.db")
print("DB en:", DB_PATH)

# ====== APP & DB ======
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_PATH}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# ====== AUTH ======
auth = HTTPBasicAuth()

# ====== MODELO ======
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    usuario = db.Column(db.String(80), unique=True, nullable=True)       # nombre de usuario para login
    password_hash = db.Column(db.String(200), nullable=True)             # hash de contraseña

with app.app_context():
    db.create_all()

# ====== ENDPOINTS BÁSICOS ======
@app.route("/")
def home():
    return "API REST PFO2 funcionando 🚀"

@app.route("/usuarios", methods=["GET"])
def get_usuarios():
    usuarios = Usuario.query.all()
    return jsonify([{"id": u.id, "nombre": u.nombre, "email": u.email} for u in usuarios])

@app.route("/usuarios", methods=["POST"])
def create_usuario():
    data = request.get_json(force=True)
    if not data.get("nombre") or not data.get("email"):
        return jsonify({"error": "nombre y email son obligatorios"}), 400

    # email único
    if Usuario.query.filter_by(email=data["email"]).first():
        return jsonify({"error": "email ya registrado"}), 409

    nuevo = Usuario(nombre=data["nombre"], email=data["email"])
    db.session.add(nuevo)
    db.session.commit()
    return jsonify({"mensaje": "Usuario creado con éxito"}), 201

# ====== REGISTRO / LOGIN ======
@app.route("/registro", methods=["POST"])
def registro():
    """
    Crea un usuario con credenciales para login.
    JSON esperado: {"usuario": "...", "password": "...", "nombre": "...", "email": "..."}
    """
    data = request.get_json(force=True)
    usuario = (data.get("usuario") or "").strip()
    password = (data.get("password") or "").strip()
    nombre = (data.get("nombre") or "").strip()
    email = (data.get("email") or "").strip()

    if not usuario or not password or not nombre or not email:
        return jsonify({"error": "usuario, password, nombre y email son obligatorios"}), 400

    if Usuario.query.filter_by(usuario=usuario).first():
        return jsonify({"error": "usuario ya existe"}), 409
    if Usuario.query.filter_by(email=email).first():
        return jsonify({"error": "email ya registrado"}), 409

    u = Usuario(
        usuario=usuario,
        password_hash=generate_password_hash(password),
        nombre=nombre,
        email=email,
    )
    db.session.add(u)
    db.session.commit()
    return jsonify({"mensaje": "Registro exitoso"}), 201

@app.route("/login", methods=["POST"])
def login():
    """
    Verifica credenciales.
    JSON: {"usuario": "...", "password": "..."}
    """
    data = request.get_json(force=True)
    usuario = (data.get("usuario") or "").strip()
    password = (data.get("password") or "").strip()

    u = Usuario.query.filter_by(usuario=usuario).first()
    if u and check_password_hash(u.password_hash, password):
        return jsonify({"mensaje": "Login exitoso"}), 200
    return jsonify({"error": "Credenciales inválidas"}), 401

# ====== BASIC AUTH PARA /tareas ======
@auth.verify_password
def verify_password(username, password):
    u = Usuario.query.filter_by(usuario=username).first()
    if u and check_password_hash(u.password_hash, password):
        return username  
    return None

@app.route("/tareas", methods=["GET"])
@auth.login_required
def tareas():
    user = auth.current_user()
    # Devuelve html
    return f"<h1>Bienvenido/a {user} a la API de Tareas</h1>"

if __name__ == "__main__":
    app.run(debug=True)
