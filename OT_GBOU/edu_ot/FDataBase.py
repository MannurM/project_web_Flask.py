import sqlite3
import time
import math
# import re
# from flask import url_for


class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def getCourse(self):  # id_course     f'{}'
        try:
            self.__cur.execute(f"SELECT theme, edu_materials, exsersis, exzamen FROM courses")
            res = self.__cur.fetchone()
            if res:
                return res

        except sqlite3.Error as e:
            print("Ошибка получения курса из БД " + str(e))
        return False

    def getStatus(self):
        try:
            self.__cur.execute(f"SELECT name, firstname, lastname, status_course, count_prob FROM users")
            res = self.__cur.fetchone()
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка получения статуса " + str(e))
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
            self.__cur.execute(f"SELECT * FROM users WHERE name = '{name}' LIMIT 1")
            res = self.__cur.fetchone()
            if not res:
                print("Пользователь не найден")
                return False
            return res
        except sqlite3.Error as e:
            print("Ошибка получения данных из БД " + str(e))
        return False