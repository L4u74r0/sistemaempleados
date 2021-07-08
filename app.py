# Desde donde manejamos todo

from flask import Flask
from flask import render_template
from flaskext.mysql import MySQL


import numpy as np # importo esto pero de prueba.  ##### BORRAR ###



app = Flask(__name__) #instanciamos flask
mysql = MySQL()
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_DB']='sistema2123'
mysql.init_app(app)




@app.route('/')
def index():
    sql = "INSERT INTO `empleados` (`id`, `nombre`, `correo`, `foto`) VALUES (NULL, 'Diosa', 'Obama@cieudad.com.ar', 'Fotolorenzzetti.jpg')";
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    return render_template('empleados/index.html')

if __name__=='__main__':
    app.run(debug=True)

#ESTOY MODIFICANDO ALGO QUE NO SE A DONDE VA
