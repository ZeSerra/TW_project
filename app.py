from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import MySQLdb
app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'zeze'
app.config['MYSQL_DB'] = 'bank'

mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('bank_web.html')
    
@app.route('/main_page', methods=['GET', 'POST'])
def main_page():
    if request.method == 'POST':
        details = request.form
        username = details['username']
        password = details['password']
        cur = mysql.connection.cursor()
        cur.execute("SELECT username from clients where username = '%s'and password = '%s'", (username, password))
        answer = cur.fetchone()
        mysql.connection.commit()
        cur.close()
        if(answer == username):
            return render_template('main_page.html')
    return render_template('main_page.html')