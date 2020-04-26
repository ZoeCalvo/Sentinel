import mysql.connector
import os
from datetime import datetime
from src.statistics_formulas import *
user_db = os.getenv('USER_DB')
pass_db = os.getenv('PASSWD_DB')
mydb = mysql.connector.connect(host="localhost", user=user_db, passwd=pass_db, database="telusko")

mycursor = mydb.cursor()


def _float64_to_mysql(value):
    value=round(value, 9)
    return float(value)

def register_users(data):
    sql = ("INSERT INTO register(name, surname, user, passwd) VALUES(%s,%s, %s, %s)")
    name = data.get('name')
    surname = data.get('surname')
    username = data.get('user')
    passwd = data.get('passwd')
    val = (name, surname, username, passwd)
    mycursor.execute(sql, val)
    mydb.commit()
    # print(mycursor.rowcount, "record inserted.")
    return 'OK'

def get_user(data):
    mycursor.execute("SELECT user, passwd FROM register");
    result = mycursor.fetchall()
    user_register = False
    for r in result:
        if (data.get('username') == r[0] and data.get('passwd') == r[1]):
            user_register = True

    return user_register




def insert_dataHashtags(hashtag, data, text, score, list_scores):
    analysis_score = _float64_to_mysql(score)
    sql = ("INSERT INTO datahashtags(hashtag, text, date, analysis_score) VALUES (%s, %s, %s, %s)")
    date = datetime.strptime(data._json['created_at'], '%a %b %d %H:%M:%S %z %Y').strftime('%d-%m-%Y')
    val = (hashtag, text, date, analysis_score)
    mycursor.execute(sql, val)
    mydb.commit()
    insert_statistics(hashtag, list_scores)
    return 'OK'


def insert_dataUsersTw(user, data, text, score, list_score):
    analysis_score = _float64_to_mysql(score)
    sql = ("INSERT INTO datausertw(user, text, date, analysis_score) VALUES (%s, %s, %s, %s)")
    date = datetime.strptime(data._json['created_at'], '%a %b %d %H:%M:%S %z %Y').strftime('%d-%m-%Y')
    val = (user, text, date, analysis_score)
    mycursor.execute(sql, val)
    mydb.commit()
    insert_statistics(user, list_score)
    return 'OK'


def insert_dataWord(word, data, text, score, list_score):
    analysis_score = _float64_to_mysql(score)
    sql = ("INSERT INTO dataword(word, text, date, analysis_score) VALUES (%s, %s, %s, %s)")
    date = datetime.strptime(data._json['created_at'], '%a %b %d %H:%M:%S %z %Y').strftime('%d-%m-%Y')
    val = (word, text, date, analysis_score)
    mycursor.execute(sql, val)
    mydb.commit()
    insert_statistics(word, list_score)

    return 'OK'


def insert_statistics(id, analysis_score):
    mean, median, mode, variance, typical_deviation = calculateStats(analysis_score)
    mean = _float64_to_mysql(mean)
    median = _float64_to_mysql(median)
    mode = _float64_to_mysql(mode)
    variance = _float64_to_mysql(variance)
    typical_deviation = _float64_to_mysql(typical_deviation)
    sql = ("SELECT * FROM statistics WHERE idstatistics = %s");
    val = (id,);
    mycursor.execute(sql, val)
    r = mycursor.fetchall()
    if r == []:
        sql = ("INSERT INTO statistics(idstatistics, mean, median, mode, variance, typical_deviation) VALUES (%s, %s, %s, %s, %s, %s)")
        val = (id, mean, median, mode, variance, typical_deviation)
        mycursor.execute(sql, val)
    else:
        sql = ("UPDATE statistics SET mean=%s, median=%s, mode=%s, variance=%s, typical_deviation=%s WHERE idstatistics = %s")
        val = (mean, median, mode, variance, typical_deviation, id)
        mycursor.execute(sql, val)
    mydb.commit()

    return 'OK'

def insert_dataUsersIg(user, post, datepost, comment, analysis_score):
    analysis_score = _float64_to_mysql(analysis_score)
    sql = ("INSERT INTO datauserig(user, post, datepost, comment, analysis_score) VALUES (%s, %s, %s, %s, %s)")
    val = (user, post, datepost, comment, analysis_score)
    mycursor.execute(sql, val)
    mydb.commit()
    insert_statistics(user, analysis_score)
    return 'OK'

def select_dataHashtags(hashtag):
    sql = ("SELECT analysis_score, text FROM datahashtags WHERE hashtag = %s")
    val = (hashtag,)
    mycursor.execute(sql, val)
    rv = mycursor.fetchall()
    final = []
    content = {}
    for result in rv:
        content = {'analysis_score': result[0], 'text': result[1]}
        final.append(content)
        content = {}
    return final

def select_dataUserTw(user):
    sql = ("SELECT analysis_score, text FROM datausertw WHERE user = %s")
    val = (user,)
    mycursor.execute(sql, val)
    rv = mycursor.fetchall()
    final = []
    content = {}
    for result in rv:
        content = {'analysis_score': result[0], 'text': result[1]}
        final.append(content)
        content = {}
    return final

def select_dataWord(word):
    sql = ("SELECT analysis_score, text FROM dataword WHERE word = %s")
    val = (word,)
    mycursor.execute(sql, val)
    rv = mycursor.fetchall()
    final = []
    content = {}
    for result in rv:
        content = {'analysis_score': result[0], 'text': result[1]}
        final.append(content)
        content = {}
    return final

def select_dataUserIg(user):
    sql = ("SELECT analysis_score, comment FROM datauserig WHERE user = %s")
    val = (user,)
    mycursor.execute(sql, val)
    rv = mycursor.fetchall()
    final = []
    content = {}
    for result in rv:
        content = {'analysis_score': result[0], 'text': result[1]}
        final.append(content)
        content = {}
    return final

def select_statistics(id):
    sql = ("SELECT * FROM statistics WHERE id = %s")
    val = (id,)
    mycursor.execute(sql, val)
    result = mycursor.fetchall()
    return result


