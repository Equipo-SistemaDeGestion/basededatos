from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Lismary_2020'
app.config['MYSQL_DB'] = 'basededatos'
mysql = MySQL(app)


@app.route('/')
def registro_usuarios():
    return render_template('registro_usuarios.html')


@app.route('/registro', methods=['POST'])
def registro():
        usuario = request.form['usuario']
        correo = request.form['correo']
        contraseña = request.form['contraseña']
        nivel_usuario = request.form['nivel_usuario']
        cur = mysql.connection.cursor()
      
        cur.execute('INSERT INTO usuarios (usuario, correo, contraseña, nivel_usuario) VALUES (%s, %s, %s, %s)',
                    (usuario, correo, contraseña, nivel_usuario))
        
        mysql.connection.commit()
        cur.close()
        
        return render_template('registro_usuarios.html', mensaje='Registro Exitoso')
    
    
if __name__ == '__main__':
        app.run(port=3000, debug=True)