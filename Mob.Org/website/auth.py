from flask import Blueprint, redirect, render_template, request,url_for
auth = Blueprint('auth',__name__)

@auth.route('/login',methods=['GET','POST'])
def login():
    return render_template("login.html")

@auth.route('/register')
def register():
    return "register"

@auth.route('/logout')
def logout():
    return "logout"