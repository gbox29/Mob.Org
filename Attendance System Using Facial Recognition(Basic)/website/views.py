from flask import Blueprint, redirect, render_template,request,session,url_for,flash
from . import mysql
views = Blueprint('views',__name__)

@views.route('/')
def home():
    return "hello views"