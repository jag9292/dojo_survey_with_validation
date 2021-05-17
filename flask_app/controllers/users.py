from flask import render_template, request, redirect, flash
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/result", methods=['POST'])
def create_user():
    if not User.validate_user(request.form):
        return redirect('/')

    User.add(request.form)
    return redirect('/result')

@app.route("/result")
def result():
    mysql = connectToMySQL('survey')
    users = mysql.query_db('SELECT * FROM users;')
    return render_template("result.html", all_users = users)
