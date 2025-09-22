from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Inicializar la app
app = Flask(__name__)

# Configuración de la base de datos SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pfo2.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo de ejemplo: Usuario
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

# Crear la base de datos
with app.app_context():
    db.create_all()

# Endpoint raíz
@app.route('/')
def home():
    return "API REST PFO2 funcionando 🚀"

# Endpoint para listar todos los usuarios
@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    usuarios = Usuario.query.all()
    return jsonify([{"id": u.id, "nombre": u.nombre, "email": u.email} for u in usuarios])

# Endpoint para crear un usuario
@app.route('/usuarios', methods=['POST'])
def create_usuario():
    data = request.json
    nuevo = Usuario(nombre=data['nombre'], email=data['email'])
    db.session.add(nuevo)
    db.session.commit()
    return jsonify({"mensaje": "Usuario creado con éxito"}), 201

if __name__ == '__main__':
    app.run(debug=True)
