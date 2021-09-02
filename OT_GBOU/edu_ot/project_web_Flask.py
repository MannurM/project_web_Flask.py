# utf-8
import os
import sqlite3

from flask import request, Flask, render_template, url_for, redirect, flash, session, g, send_file
from flask_login import LoginManager, login_user, login_required
# from flask_security import RoleMixin
from werkzeug.security import generate_password_hash, check_password_hash

from FDataBase import FDataBase
from UserLogin import UserLogin


# конфигурация
DATABASE = '/tmp/pr_ot.db'
DEBUG = True
SECRET_KEY = 'fdgfh78@#5?>gfhf89dx,v06k'

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path,'pr_ot.db')))


login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = "Авторизуйтесь для доступа к закрытым страницам"
login_manager.login_message_category = "success"


@login_manager.user_loader
def load_user(user_id):
    # print('load_user_')
    return UserLogin().fromDB(user_id, dbase)


def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn

def create_db():
    """Вспомогательная функция для создания таблиц БД"""
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()

def get_db():
    '''Соединение с БД, если оно еще не установлено'''
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


dbase = None
@app.before_request
def before_request():
    """Установление соединения с БД перед выполнением запроса"""
    global dbase
    db = get_db()
    dbase = FDataBase(db)


@app.teardown_appcontext
def close_db(error):
    '''Закрываем соединение с БД, если оно было установлено'''
    if hasattr(g, 'link_db'):
        g.link_db.close()


@app.route('/')
@app.route('/index.html')
def index():
    return render_template(url_for('index'))


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = dbase.getUserByName(request.form['name'])
        #  проверки в базе
        if not user:
            flash('ОШИБКА, проверьте фамилию и пароль')
            return render_template(url_for('index'))

        if check_password_hash(user['hpsw'], request.form['psw']):
            userLogin = UserLogin().create(user)
            login_user(userLogin)
            session['name'] = request.form['name']
            return redirect(url_for('courses'))
        else:
            flash('ОШИБКА, проверьте фамилию и пароль')
            return render_template(url_for('login'))
    return render_template(url_for('index'))


@app.route('/logout')
def logout():
    # удаляем имя пользователя из сеанса, если оно есть
    session.pop('username', None)
    return redirect(url_for('index'))


@app.route('/courses')
@login_required
def courses():
    db = get_db()
    dbase = FDataBase(db)
    theme, edu_materials, exsersis, exzamen = dbase.getCourse()
    name, firstname, lastname, status, count_prob = dbase.getStatus()
    if status == 1:
        status = 'Сдано'
    else:
        status = 'Не сдано'
    return render_template('courses.html', theme=theme, edu_materials=edu_materials,
                           exsersis=exsersis, exzamen=exzamen, status=status, count_prob=count_prob,
                           name=name, firstname=firstname, lastname=lastname)


@app.route('/edu_mat')
@login_required
def edu_mat():
    db = get_db()
    dbase = FDataBase(db)
    theme, edu_materials, exsersis, exzamen = dbase.getCourse()
    name, firstname, lastname, status_course, count_prob = dbase.getStatus()
    return render_template('edu_mat.html', theme=theme,edu_materials=edu_materials, exsersis=exsersis, exzamen=exzamen,
                           name=name, firstname=firstname, lastname=lastname)


@app.route('/edu_test')
@login_required
def edu_test():
    exsersis, exzamen = dbase.getCourse()
    return render_template('edu_test.html')


@app.route('/edu_exz')
@login_required
def edu_exz():
    exzamen = dbase.getCourse()
    return render_template('edu_exz.html')


@app.route("/exit")
def exit():
    return render_template('exit.html')


if __name__ == '__main__':
    app.run(debug=True)
