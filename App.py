from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app= Flask(__name__)

#Mysqlconecction
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='pythoncrud'
mysql=MySQL(app)

#inicializar una sesion
app.secret_key = 'mysecretkey'




@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts')
    data = cur.fetchall()
    return render_template('index.html', contacts=data)

@app.route('/add_contact', methods = ['POST'])
def add_contac():
   if request.method == 'POST':
       fullname = request.form['fullname']
       phone = request.form['phone']
       email = request.form['email']
       cur = mysql.connection.cursor()
       cur.execute('INSERT INTO contacts (fullname, phone, email) VALUES( %s, %s, %s)',
       (fullname, phone, email))
       mysql.connection.commit()
       flash('Contacto añadido satisfactoriamente')

       print(fullname)
       print(phone)
       print(email)

       return redirect(url_for('Index'))
    

@app.route('/edit')
def edit_contact():
    return 'Edit Contact'

@app.route('/delete')
def delete_contact():
    return 'Delete Contact'


if __name__ == '__main__':
     app.run(port=3000,debug=True)