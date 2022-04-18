from flask import Blueprint, render_template, request,flash,redirect,url_for,session
from . import mysql
auth = Blueprint('auth',__name__)

@auth.route('/login', methods = ['GET','POST'])
def login():
    pass