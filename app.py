from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

# ====== Configuración de rutas y base de datos ======
BASE_DIR = os.path.abspath(os.path.dirname(__file__))     # carpeta actual del proyecto
DB_PATH = os.path.join(BASE_DIR, "pfo2.db")               # pfo2.db en la misma carpeta
print("DB en:", DB_PATH)                                  # para ver dónde se guarda

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_PATH}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# ====== Modelo ======
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

# ====== Crear tablas si no existen ======
with app.app_context():
    db.create_all()

# ====== Endpoints ======
@app.route('/')
def home():
    return "API REST PFO2 funcionando 🚀"

@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    usuarios = Usuario.query.all()
    return jsonify([{"id": u.id, "nombre": u.nombre, "email": u.email} for u in usuarios])

@app.route('/usuarios', methods=['POST'])
def create_usuario():
    data = request.get_json(force=True)
    nuevo = Usuario(nombre=data['nombre'], email=data['email'])
    db.session.add(nuevo)
    db.session.commit()
    return jsonify({"mensaje": "Usuario creado con éxito"}), 201

if __name__ == '__main__':
    app.run(debug=True)
