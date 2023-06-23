from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(host="localhost",
  user="root",
  password="Lismary_2020",
  database="basededatos"
)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    usuario = request.form['usuario']
    contraseña = request.form['contraseña']
    # Consulta a la base de datos para verificar el usuario y contraseña
    cur = mydb.cursor()
    
    cur.execute("SELECT * FROM usuarios WHERE usuario = %s AND contraseña = %s", (usuario, contraseña))
    
    user = cur.fetchone()

    if user:
        # Usuario y contraseña correctos, redirigir a otro formulario
        return redirect('/bienvenidos')
    else:
        # Usuario o contraseña incorrectos, mostrar mensaje de error
        return render_template('login.html', error='Usuario o contraseña incorrectos')

@app.route('/formulario')
def formulario():
    return render_template('formulario.html')

if __name__ == '__main__':
        app.run(port=5000, debug=True)