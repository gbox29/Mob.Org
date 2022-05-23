from flask import Blueprint, redirect, render_template, request, session,url_for
views = Blueprint('views',__name__)
from . import mysql

##user side
@views.route('/')
def index():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM t_item WHERE id = 1")
    if resultValue > 0:
        userDetails = cur.fetchall()
        result = cur.execute("SELECT * FROM t_item LIMIT 5")
        if result > 0:
            details = cur.fetchall()
        if 'username' in session:
            username = "username"
            return render_template("index.html",userDetails=userDetails,details=details,username=username)
        else:
            return render_template("index.html",userDetails=userDetails,details=details)


@views.route('/view_item/<string:id_data>',methods=['GET','POST'])
def view_item(id_data):
    cur = mysql.connection.cursor()
    itemDetails = cur.execute("SELECT * FROM t_item WHERE id =%s",(id_data))
    itemDetails = cur.fetchone()
    if itemDetails:
        if 'username' and 'user_id' in session:
            username = "username"
            if request.method == 'POST':
                status = request.form['status']
                start_date = request.form['start_date']
                end_date = request.form['end_date']
                ep_seen = request.form['ep_seen']
                rating = request.form['rating']
                user_id = session['user_id']
                if ep_seen > itemDetails[3]:
                    pass
                else:
                    cur.execute("""INSERT INTO t_list (user_id,item_id,start_date,end_date,ep_seen,rating,list_status)
                                    VALUES (%s,%s,%s,%s,%s,%s,%s)""",
                            (user_id,id_data,start_date,end_date,ep_seen,rating,status))
                    mysql.connection.commit()
            return render_template("view_item.html",itemDetails=itemDetails,username=username)
        else:
            return render_template("view_item.html",itemDetails=itemDetails)
##admin side
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
        synopsis = request.form['synopsis']
        background = request.form['background']
        poster = request.form['poster']
        trailer = request.form['trailer']
        cur.execute(""" INSERT INTO 
                    t_item (item_name,t_type,episode,date_release,item_source,demographic,duration,synopsis,background,poster,trailer) 
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) """,(name,type,episode,date,source,demographic,duration,synopsis,background,poster,trailer))
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
            synopsis = request.form['synopsis']
            background = request.form['background']
            poster = request.form['poster']
            trailer = request.form['trailer']
            cur.execute(""" UPDATE t_item SET item_name=%s, episode=%s,date_release=%s,item_source=%s,
                        demographic=%s,duration=%s,synopsis=%s,background=%s,poster=%s,trailer=%s WHERE id=%s""",
                        (name,episode,date,source,demographic,duration,synopsis,background,poster,trailer,id_data))
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







