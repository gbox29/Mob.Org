from flask import Blueprint, redirect, render_template, request,url_for
views = Blueprint('views',__name__)
from . import mysql

@views.route('/admin_base')
def home():
    return render_template("admin_base.html")
@views.route('/add_film', methods=['GET','POST'])
def add_film():
    cur = mysql.connection.cursor()
    if request.method == 'POST':
        name = request.form['item_name']
        type = "film"
        episode = request.form['episode']
        date = request.form['date']
        source = request.form['source']
        demographic = request.form['demographic']
        duration = request.form['duration']
        poster = request.form['poster']
        trailer = request.form['trailer']
        cur.execute(""" INSERT INTO 
                    t_item (item_name,t_type,episode,date_release,item_source,demographic,duration,poster,trailer) 
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s) """,(name,type,episode,date,source,demographic,duration,poster,trailer))
        mysql.connection.commit()
        return redirect(url_for("views.film_table"))
    return render_template("add_film.html")

@views.route('/film_table')
def film_table():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("Select * FROM t_item")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template("table_film.html",userDetails=userDetails)
    return render_template("table_film.html")

@views.route('/update_film/<string:id_data>', methods=['GET','POST'])
def update_film(id_data):
   cur = mysql.connection.cursor()
   resultValue = cur.execute("Select * FROM t_item WHERE id = %s",(id_data))
   if resultValue > 0:
        userDetails = cur.fetchall()
        if request.method == 'POST':
            name = request.form['item_name']
            episode = request.form['episode']
            date = request.form['date']
            source = request.form['source']
            demographic = request.form['demographic']
            duration = request.form['duration']
            poster = request.form['poster']
            trailer = request.form['trailer']
            cur.execute(""" UPDATE t_item SET item_name=%s, episode=%s,date_release=%s,item_source=%s,
                        demographic=%s,duration=%s,poster=%s,trailer=%s WHERE id=%s""",
                        (name,episode,date,source,demographic,duration,poster,trailer,id_data))
            mysql.connection.commit()
            return redirect(url_for("views.film_table"))
        return render_template("update_film.html",userDetails=userDetails)
   return render_template("update_film.html")

@views.route('/delete_film/<string:id_data>')
def delete_film(id_data):
    cur = mysql.connection.cursor()
    cur.execute(""" DELETE FROM t_item WHERE id=%s""",(id_data))
    cur.execute("ALTER TABLE t_item AUTO_INCREMENT = 1")
    mysql.connection.commit()
    return redirect(url_for("views.film_table"))







