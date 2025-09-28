PFO2_PSRedes_SabrinaChoque_ComisionD

Alumno: Sabrina Choque  
Comisión: D  

gitHub:   


El objetivo de este proyecto es implementar una **API REST** con Python y Flask, que se conecta a una base de datos **SQLite**.  
Además, desarrollamos un **cliente en consola** que permite interactuar con la API para crear y listar usuarios.

Con este trabajo entendimos cómo:
- Establecer endpoints REST básicos.
- Guardar y recuperar datos persistentes en una base de datos.
- Conectar un cliente a la API y probar su funcionamiento.

Archivos utilizados en Python

- **app.py** → servidor Flask que expone la API REST.  
- **cliente_api.py** → cliente en consola para interactuar con la API.  
- **pfo2.db** → base de datos SQLite generada automáticamente al correr el servidor.  

Pasos de ejecución

1. Crear y activar entorno virtual (venv)
En la carpeta del proyecto, abrir una terminal y ejecutar:

Windows (PowerShell):
python -m venv venv
venv\Scripts\activate

2. Instalar dependencias
pip install flask flask_sqlalchemy requests

3. Iniciar el servidor (API)
python app.py
El servidor corre en: http://127.0.0.1:5000/
![alt text](image.png)
![alt text]({339E5BB6-5390-4417-9EE0-9EFE1763C068}.png)

4. Probar con el cliente en otra terminal
Abrir otra terminal (con el venv activado) y ejecutar:
python cliente_api.py
En el cliente podés crear un usuario y listar usuarios.
![alt text]({B49090BE-1ACD-48F4-B8B0-CDBEF7AB5DA4}.png)
![alt text]({2963B49F-7A60-4A2B-B404-454C1C49532F}.png)
![alt text]({A0ABD292-55F0-4566-8CAC-90E5A5B77EB9}.png)
![alt text]({57CDE9CD-CC91-48C7-B8F7-615E2A371E87}.png)

5. Ver usuarios desde el navegador
http://127.0.0.1:5000/usuarios
![alt text]({46D36A97-1E84-4E6E-9BF6-224ABB346175}.png)

6. Base de datos SQLite

La base de datos se genera automáticamente con el nombre **pfo2.db**.  
En ella se almacenan los usuarios creados desde el cliente o el navegador.

Podemos comprobar su existencia ejecutando en la terminal:
dir *.db
![alt text]({4C4200B0-1BD1-4762-9174-9DA66AF83F8C}.png)