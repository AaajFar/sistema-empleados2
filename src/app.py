from flask import Flask
from flask import render_template
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Ab36949661'
app.config['MYSQL_DATABASE_DB'] = 'empleados2'

mysql.init_app(app)

@app.route('/')
def index():
    conn = mysql.connect()
    cursor = conn.cursor()

    sql = "insert into empleados (nombre, correo, foto) values ('Juan', 'juan@email.com', 'fotodejuan.jpg');"
    cursor.execute(sql)

    conn.commit()

    return render_template('empleados/index.html')

@app.route('/create')
def create():
    
    return render_template('empleados/create.html')

if __name__ == '__main__':
    app.run(debug=True)
