

#@app.route('/courses')
# @login_required
# def courses(id_course):
#     db = get_db()
#     dbase = FDataBase(db)
#     themes, edu_materials, exzersis, exzamen = dbase.getCourses(id_course)
#     return render_template('courses.html', themes=main.themes)



# !!! Секретная сессия пользователя
#from flask import session
# установим секретный ключ для подписи. Держите это в секрете!
# app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
#


# @app.route('/profile/<username>')
# def profile(username):
#     return f'профиль пользователя {username}'
#
#
# app.errorhandler(404)
# def pageNotFound(error):
#     return render_template('page404.html', title='Страница не найдена'), 404
#
#
# @app.route('/user/<string:name>/<int:id>')
# def user(name, id):
#     return 'User page ' + name + '-' + str(id)


# !!! Чтение файлов  куки
# from flask import request
#
# @app.route('/')
# def index():
#     # Используйте `request.cookies.get(key)` вместо `cookies[key]`,
#     # чтобы не получать `KeyError`, если cookie отсутствует.
#     username = request.cookies.get('username')



# Устанвока куки
# from flask import make_response
#
# @app.route('/')
# def index():
#     response = make_response(render_template(...))
#     response.set_cookie('username', 'the username')
#     return response

# !!! Перенаправление другую страницу
# from flask import abort, redirect, url_for
#
# @app.route('/')
# def index():
#     return redirect(url_for('login'))
#
# @app.route('/login')
# def login():
#     abort(401)
#     # эта функция никогда не исполнится
#     this_is_never_executed()
# Бессмысленный пример, так как пользователь будет перенаправлен с главной страницы на страницу, к которой он не может
# получить доступ (код HTTP 401 означает отказ в доступе), но этот пример показывает, как это работает.

