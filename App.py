from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app= Flask(__name__)


app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='pythoncrud'
mysql=MySQL(app)


@app.route('/')
def Index():
    return render_template('index.html')

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

       print(fullname)
       print(phone)
       print(email)

       return 'received'
    

@app.route('/edit')
def edit_contact():
    return 'Edit Contact'

@app.route('/delete')
def delete_contact():
    return 'Delete Contact'


if __name__ == '__main__':
     app.run(port=3000,debug=True)