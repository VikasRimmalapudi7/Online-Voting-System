import sqlite3
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Nominnes
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


    return render_template('home.html', nominees=Nominnes.query.all(),user=current_user)

    

    



