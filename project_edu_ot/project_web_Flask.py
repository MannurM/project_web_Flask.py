# utf-8
import os
import sqlite3

from flask import request, Flask, render_template, url_for,  redirect, flash, session, g
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


@app.route('/lp')
def lp():
    print(url_for('lp'))
    return render_template('lp.html') #
    # return render_template(url_for('lp'))


@app.route('/')
@app.route('/index.html')
def index():
    return render_template(url_for('index'))


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = dbase.getUserByEmail(request.form['email'])

        # user_name = dbase.getUserByName(request.form['name'])   TODO добавить форму по фамилии? тогда изменить форму
        #  проверки в базе
        if not user:
            flash('ОШИБКА, проверьте электронную почту и пароль')
            return render_template(url_for('login'))
        if check_password_hash(user['hpsw'], request.form['psw']):
            userLogin = UserLogin().create(user)
            login_user(userLogin)
            session['email'] = request.form['email']
            return redirect(url_for('courses'))
        else:
            flash('ОШИБКА, проверьте электронную почту и пароль')
            return render_template(url_for('login'))
    return render_template(url_for('index'))


@app.route('/logout')
def logout():
    # удаляем имя пользователя из сеанса, если оно есть
    session.pop('username', None)
    return redirect(url_for('index'))


@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        if len(request.form['name']) > 4 and len(request.form['email']) > 4 \
            and len(request.form['psw']) > 4 and request.form['psw'] == request.form['psw2']:
            hash = generate_password_hash(request.form['psw'])
            res = dbase.addUser(request.form['name'], request.form['firstname'], request.form['lastname'],
                                request.form['dateborn'], request.form['email'], hash)
            if res:
                flash("Вы успешно зарегистрированы", "success")
                return redirect(url_for('courses'))
            else:
                flash("Ошибка при добавлении в БД", "error")
                return redirect(url_for('register'))
        else:
            flash("Неверно заполнены поля", "error")
            return redirect(url_for('register'))

    return render_template('registration.html')  # (url_for('register'))


@app.route('/choise_course')
@login_required
def choise_course():


@app.route('/courses')
@login_required
def courses():
    db = get_db()
    dbase = FDataBase(db)
    theme_list = dbase.getCourseAnonce()
    return render_template('courses.html', theme_list=theme_list)
# , edu_materials=edu_materials, exsersis=exsersis, exzamen=exzamen


# @app.route("/addCourse")
# def addCourse():
#     if request.method == "POST":
#         if len(request.form['name']) > 4:
#             res = dbase.addCourse(request.form['theme'], request.form['edu_materials'], request.form['exzersis'],
#                                   request.form['exzamen'])
#             if not res:
#                 flash('Ошибка добавления Курса', category = 'error')
#             else:
#                 flash('Курс добавлен успешно', category='success')
#         else:
#             flash('Ошибка добавления Курса', category='error')
#
#     return render_template(url_for('addCourse.html'))


@app.route("/exit")
def exit():
    return render_template('exit.html')


if __name__ == '__main__':
    app.run(debug=True)
