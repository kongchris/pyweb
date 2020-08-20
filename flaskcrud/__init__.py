from flask import Flask, render_template,request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.secret_key = "key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kmh.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    email = db.Column(db.String(200))
    tel = db.Column(db.Integer)

    def __init__(self, username, email, tel):
        self.username = username
        self.email = email
        self.tel = tel

@app.route('/')
def index():
    all_data = Employee.query.all() #select * from employee
    return render_template("index.html", employees=all_data)

@app.route('/insut',methods=['POST'])
def insut():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        tel = request.form['tel']

        insertUser = Employee(username,email,tel)
        db.session.add(insertUser)
        db.session.commit()
        
        return redirect(url_for('index'))

    @app.route('/delete/<uid>')
    def delete(uid):
        delUser = Employee.query.get(uid)
        db.session.delete(delUser)
        db.session.commit()

        return redirect(url_for('index'))

    @app.route('/update', methods={'POST'})
    def update():
        updateUser = Employee.query.get(request.form.get('id'))
        updateUser.username = request.form['username']
        updateUser.email = request.form['email']
        updateUser.tel = request.form['tel']
        return redirect(url_for('index'))

