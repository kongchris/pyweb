<<<<<<< HEAD
# -*-coding: utf-8 -*-
# from gtts import gTTS
# from playsound import playsound
from flask import Flask, render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "Secret Key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shindalsoo.db'
=======
from flask import Flask, render_template,request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.secret_key = "key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kmh.db'
>>>>>>> d490fc19aa69463eece301de912b82d2c808827c
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Employee(db.Model):
<<<<<<< HEAD
    userid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100))
    email = db.Column(db.String(200))
    tel = db.Column(db.String(50))
=======
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    email = db.Column(db.String(200))
    tel = db.Column(db.Integer)
>>>>>>> d490fc19aa69463eece301de912b82d2c808827c

    def __init__(self, username, email, tel):
        self.username = username
        self.email = email
        self.tel = tel

@app.route('/')
def index():
<<<<<<< HEAD
    all_data = Employee.query.order_by(Employee.userid.desc()).all() # select * from employee
    return render_template("index.html", employees=all_data)

@app.route('/insert', methods=['POST'])
def insert():
=======
    all_data = Employee.query.all() #select * from employee
    return render_template("index.html", employees=all_data)

@app.route('/insut',methods=['POST'])
def insut():
>>>>>>> d490fc19aa69463eece301de912b82d2c808827c
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        tel = request.form['tel']

        insertUser = Employee(username,email,tel)
        db.session.add(insertUser)
        db.session.commit()
<<<<<<< HEAD

        return redirect(url_for('index'))

@app.route('/delete/<uid>')
def delete(uid):
    delUser = Employee.query.get(uid) # select * from Employee where userid=3
    db.session.delete(delUser)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/update', methods=['POST'])
def update():
    if request.method == 'POST':
        updateUser = Employee.query.get(request.form.get('userid'))
        updateUser.username = request.form['username']
        updateUser.email = request.form['email']
        updateUser.tel = request.form['tel']
        db.session.commit()
        return redirect(url_for('index'))

@app.route('/search', methods=['POST'])
def search():
    txtsearch = request.form['txtsearch']
    searchUser = Employee.query.filter(Employee.username.contains(txtsearch))
    return render_template("index.html", employees=searchUser, txtsearch=txtsearch)

@app.route('/playmp3')
def playmp3():
    text = "오늘은, 2020년 8월 20일입니다. 고양이가 소리를 내려고합니다. 우리모두 스마트고양이를 응원합시다~~람쥐"
    filename = "hellosmartcat.mp3"
    tts = gTTS(text=text, lang='ko')
    tts.save(filename)
    playsound(filename)

    return "고양이가 소리를 냈습니다."
=======
        
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

>>>>>>> d490fc19aa69463eece301de912b82d2c808827c
