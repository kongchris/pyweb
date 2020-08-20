-*- coding: utf-8 -*- 
from gtts import gTTS
from playsound import palysound
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
    tel = db.Column(db.String(300))

    def __init__(self, username, email, tel,list):
        self.username = username
        self.email = email
        self.tel = tel
        self.list = list

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
        list = request.form['list']

        insertUser = Employee(username,email,tel,list)
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
    list = request.form['list']
    return redirect(url_for('index'))

@app.route('/search',methods=['POST'])
def search():
    txt = request.form['textsueach']
    su = Employee.query.filter(Employee.Name.contains(Employee.username.co))
    return render_template("index.html", employees=su, searchUser=txt)

    @app.route('/palymp3')
    def playsound():
        text = "고양이가 소리를 내려고 합니다 우리모두 SMCT 를 응원합시다"
        filename="aa.mp3"
        tts = gTTS(text=text, lang='ko')
        tts.save(filename)
        playsound(filename)
        return"sound"