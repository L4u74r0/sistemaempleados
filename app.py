# Desde donde manejamos todo

from flask import Flask
from flask import render_template, request
from flaskext.mysql import MySQL
from pymysql import cursors

app = Flask(__name__) #instanciamos flask
mysql = MySQL()
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_DB']='sistema2123'
mysql.init_app(app)




@app.route('/')
def index():
    sql = "INSERT INTO `empleados` (`id`, `nombre`, `correo`, `foto`) VALUES (NULL, 'Messi', 'Messi@cieudad.com.ar', 'Messi.jpg')";
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    return render_template('empleados/index.html')


@app.route('/create')
def create():
   return render_template('empleados/create.html')


@app.route('/store', methods=['POST'])
def storage():
   _Nombre=request.form['txtNombre']
   _Correo=request.form['txtCorreo']
   _Foto=request.files['txtFoto'] 
   sql = "INSERT INTO `empleados` (`id`, `nombre`, `correo`, `foto`) VALUES (NULL,%s,%s,%s);"
   datos=(_Nombre, _Correo, _Foto.filename)

   conn=mysql.connect()
   cursor=conn.cursor()
   cursor.execute(sql, datos)
   conn.commit()
   return render_template('empleados/index.html')





if __name__=='__main__':
    app.run(debug=True)

