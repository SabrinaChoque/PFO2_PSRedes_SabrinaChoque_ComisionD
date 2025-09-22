# cliente_api.py
import requests

BASE = "http://127.0.0.1:5000"

def crear_usuario():
    nombre = input("Nombre: ").strip()
    email = input("Email: ").strip()
    r = requests.post(f"{BASE}/usuarios", json={"nombre": nombre, "email": email})
    print("Status:", r.status_code)
    try:
        print("Respuesta:", r.json())
    except Exception:
        print("Texto:", r.text)

def listar_usuarios():
    r = requests.get(f"{BASE}/usuarios")
    print("Usuarios:", r.json())

def main():
    while True:
        print("\n=== Cliente API ===")
        print("1) Crear usuario")
        print("2) Listar usuarios")
        print("3) Salir")
        op = input("Opción: ").strip()
        if op == "1":
            crear_usuario()
        elif op == "2":
            listar_usuarios()
        elif op == "3":
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()
