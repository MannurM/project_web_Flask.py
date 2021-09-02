import os
import sqlite3
from flask import request, Flask, render_template, url_for, session, redirect, flash, g
from wtforms import Form, BooleanField, StringField, PasswordField, validators

# конфигурация
DATABASE = '/pr_ot.db'
DEBUG = True
SECRET_KEY = 'lmkdfjdghjdfgvn7hsduvnsdvuy5'


app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(DATABASE=os.path.join(app.root_path, 'pr_ot.db')))


def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn


def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return  g.link_db


@app.route('/')
def index():
    db = get_db()
    # dbase = FDatabase(db)
    return render_template('index.html' ) # , menu = dbase.getMenu()


@app.before_request
def before_request():
    db=get_db()


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()

