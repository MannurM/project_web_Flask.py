import sqlite3
import time
import math
# import re
# from flask import url_for


class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    # def addCourse(self, theme, edu_materials, exzersis, exzamen):
    #     try:
    #         self.__cur.execute(f"SELECT COUNT() as `count` FROM courses WHERE theme LIKE '{theme}'")
    #         res = self.__cur.fetchone()
    #         if res['count'] > 0:
    #             print("Курс с таким theme уже существует")
    #             return False
    #
    #         # base = url_for('static', filename='images_html')
    #
    #         # text = re.sub(r"(?P<tag><img\s+[^>]*src=)(?P<quote>[\"'])(?P<url>.+?)(?P=quote)>",
    #         #               "\\g<tag>" + base + "/\\g<url>>",
    #         #               text)
    #
    #         tm = math.floor(time.time())
    #         self.__cur.execute("INSERT INTO courses VALUES(?, ?, ?, ?, ?)", (theme, edu_materials, exzersis,
    #                                                                                exzamen, tm))
    #         self.__db.commit()
    #     except sqlite3.Error as e:
    #         print("Ошибка добавления курса в БД " + str(e))
    #         return False
    #     return True

    def getCourse(self):  # id_course     f'{}'
        try:
            self.__cur.execute(f"SELECT theme, edu_materials, exsersis, exzamen FROM courses ORDER BY theme")
            res = self.__cur.fetchone()
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка получения курса из БД " + str(e))
        return False

    def choiseCourse(self, email_user):  # id_course     f'{}'
        """к пользователю зарегистрированному в users c  email_user добавить theme из таблицы courses """
        try:
            self.__cur.execute(f"UPDATE theme.users FROM theme.courses WHERE email=email_user")
            # SELECT name, sex, games.score FROM games
            # JOIN users ON games.user_id = users.rowid
            res = self.__cur.fetchone()
            print(res)
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка получения курса из БД " + str(e))
        return False


    def getCourseAnonce(self):
        try:
            self.__cur.execute(f"SELECT theme, edu_materials, exsersis, exzamen FROM courses ")
            res = self.__cur.fetchall()
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка получения курса из БД " + str(e))
        return []

    def addUser(self, name, firstname, lastname, dateborn, email, hpsw):
        try:
            self.__cur.execute(f"SELECT COUNT() as `count` FROM users WHERE email LIKE '{email}'")
            res = self.__cur.fetchone()
            if res['count'] > 0:
                print("Пользователь с таким {email} - уже существует")
                return False

            tm = math.floor(time.time())
            self.__cur.execute("INSERT INTO users VALUES(NULL, ?, ?, ?, ?, ?, ?, ?)", (name, firstname, lastname,
                                                                                       dateborn, email, hpsw, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Ошибка добавления пользователя в БД " + str(e))
            return False

        return True

    def getUser(self, user_id):
        try:
            self.__cur.execute(f"SELECT * FROM users WHERE id = {user_id} LIMIT 1")
            res = self.__cur.fetchone()
            if not res:
                print("Пользователь не найден")
                return False
            return res
        except sqlite3.Error as e:
            print("Ошибка получения данных из БД " + str(e))
        return False

    def getUserByEmail(self, email):
        try:
            self.__cur.execute(f"SELECT * FROM users WHERE email = '{email}' LIMIT 1")
            res = self.__cur.fetchone()
            if not res:
                print("Пользователь не найден")
                return False
            return res
        except sqlite3.Error as e:
            print("Ошибка получения данных из БД " + str(e))
        return False

    def getUserByName(self, name):
        try:
            self.__cur.execute(f"SELECT * FROM users WHERE email = '{name}' LIMIT 1")
            res = self.__cur.fetchone()
            if not res:
                print("Пользователь не найден")
                return False
            return res
        except sqlite3.Error as e:
            print("Ошибка получения данных из БД " + str(e))
        return False