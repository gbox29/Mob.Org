from flask import Flask
from flask_mysqldb import MySQL

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'asdasd'
    app.secret_key = "super secret key"
    
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = ''
    app.config['MYSQL_DB'] = 'db_schedule'
    
    global mysql
    mysql = MySQL(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
   
    return app