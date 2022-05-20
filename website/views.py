import sqlite3
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from sqlalchemy import true
from .models import Nominnes, User
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
   # con = sqlite3.connect('database.db')
    #db = con.cursor()
   # db.execute('insert into user values ("Aaa", "AAA")')
   # db.execute('insert into user values ("Bbb", "BBB")')
    #res = db.execute('select * from nominnes')

    if request.method=="POST":
      print(request.form.get('note'))
        #flash(json.loads(request.data),category='error')
      # con = sqlite3.connect('database.db')
    #db = con.cursor()
    #db.execute(select user update id  set isvoted=True)
    #db.execute(select nominnes update id  SET  votes=votes+1 )

    #flash("voted succesfully",category='success)
    #logout_user()
    #return redirect(url_for('auth.home'))
    

    return render_template('home.html', nominees=Nominnes.query.all(),user=current_user)

@views.route('/update-data', methods=['POST'])
def update_data():
  print(request.form['options'])
  user = User.query.get(current_user.id)
  if user is not None:
    if user.isvoted:
      flash('You Have Already Voted.', category='error')
      return render_template('home.html',user=current_user)
    user.isvoted = True
    db.session.commit()
  nominee = Nominnes.query.get(request.form['options'])
  if nominee is not None:
    nominee.votes += 1
    db.session.commit()
  return render_template('home.html', user=current_user)







    

    



