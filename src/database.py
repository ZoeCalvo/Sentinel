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
    date = datetime.strptime(data._json['created_at'], '%a %b %d %H:%M:%S %z %Y').strftime('%Y-%m-%d')
    val = (hashtag, text, date, analysis_score)
    mycursor.execute(sql, val)
    mydb.commit()
    insert_statistics(hashtag, list_scores)
    return 'OK'


def insert_dataUsersTw(user, data, text, score, list_score):
    analysis_score = _float64_to_mysql(score)
    sql = ("INSERT INTO datausertw(user, text, date, analysis_score) VALUES (%s, %s, %s, %s)")
    date = datetime.strptime(data._json['created_at'], '%a %b %d %H:%M:%S %z %Y').strftime('%Y-%m-%d')
    val = (user, text, date, analysis_score)
    mycursor.execute(sql, val)
    mydb.commit()
    insert_statistics(user, list_score)
    return 'OK'


def insert_dataWord(word, data, text, score, list_score):
    analysis_score = _float64_to_mysql(score)
    sql = ("INSERT INTO dataword(word, text, date, analysis_score) VALUES (%s, %s, %s, %s)")
    date = datetime.strptime(data._json['created_at'], '%a %b %d %H:%M:%S %z %Y').strftime('%Y-%m-%d')
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
    datepost = datetime.strptime(datepost, '%Y-%m-%dT%H:%M:%S').strftime('%Y-%m-%d')
    sql = ("INSERT INTO datauserig(user, post, datepost, comment, analysis_score) VALUES (%s, %s, %s, %s, %s)")
    val = (user, post, datepost, comment, analysis_score)
    mycursor.execute(sql, val)
    mydb.commit()

    return 'OK'

def select_dataHashtags(hashtag, since_date, until_date):
    if since_date=='' or until_date=='':
        if until_date is not '':
            sql = ("SELECT analysis_score, text, date FROM datahashtags WHERE hashtag = %s AND date<=%s")
            val = (hashtag, until_date)
            mycursor.execute(sql, val)
        elif since_date is not '':
            sql = ("SELECT analysis_score, text, date FROM datahashtags WHERE hashtag = %s AND date>=%s")
            val = (hashtag, since_date)
            mycursor.execute(sql, val)
        else:
            sql = ("SELECT analysis_score, text, date FROM datahashtags WHERE hashtag = %s")
            val = (hashtag,)
            mycursor.execute(sql, val)
    else:
        sql = ("SELECT analysis_score, text, date FROM datahashtags WHERE hashtag = %s AND date BETWEEN %s AND %s")
        val = (hashtag, since_date, until_date)
        mycursor.execute(sql, val)
    rv = mycursor.fetchall()
    final = []
    content = {}
    for result in rv:
        content = {'analysis_score': result[0], 'text': result[1], 'date': result[2]}
        final.append(content)
        content = {}
    return final


def selectHashtagsGroupByDates(hashtag, since_date, until_date):
    if since_date=='' or until_date=='':
        if until_date is not '':
            sql = ("SELECT AVG(analysis_score), date FROM datahashtags WHERE hashtag = %s AND date<=%s GROUP BY date")
            val = (hashtag, until_date)
            mycursor.execute(sql, val)
        elif since_date is not '':
            sql = ("SELECT AVG(analysis_score), date FROM datahashtags WHERE hashtag = %s AND date>=%s GROUP BY date")
            val = (hashtag, since_date)
            mycursor.execute(sql, val)
        else:
            sql = ("SELECT AVG(analysis_score), date FROM datahashtags WHERE hashtag = %s GROUP BY date")
            val = (hashtag,)
            mycursor.execute(sql, val)
    else:
        sql = ("SELECT AVG(analysis_score), date FROM datahashtags WHERE hashtag = %s AND date BETWEEN %s AND %s GROUP BY date")
        val = (hashtag, since_date, until_date)
        mycursor.execute(sql, val)
    rv = mycursor.fetchall()
    final = []
    content = {}
    for result in rv:
        content = {'analysis_score': result[0], 'date': result[1]}
        final.append(content)
        content = {}
    return final

def selectHashtagsByIntervals(hashtag, since_date, until_date):
    if since_date=='' or until_date=='':
        if until_date is not '':
            sql = ("SELECT analysis_score FROM datahashtags WHERE hashtag = %s AND date<=%s")
            val = (hashtag, until_date)
            mycursor.execute(sql, val)
        elif since_date is not '':
            sql = ("SELECT analysis_score FROM datahashtags WHERE hashtag = %s AND date>=%s")
            val = (hashtag, since_date)
            mycursor.execute(sql, val)
        else:
            sql = ("SELECT analysis_score FROM datahashtags WHERE hashtag = %s")
            val = (hashtag,)
            mycursor.execute(sql, val)
    else:
        sql = ("SELECT analysis_score FROM datahashtags WHERE hashtag = %s AND date BETWEEN %s AND %s")
        val = (hashtag, since_date, until_date)
        mycursor.execute(sql, val)
    rv = mycursor.fetchall()
    final = []
    content = {}
    min = 1
    max = -1
    int0=0
    int1=0
    int2=0
    int3=0
    int4=0
    int5=0
    int6=0
    int7=0
    int8=0
    int9 = 0
    for result in rv:
        if min > result[0]:
            min = result[0]
        if max < result[0]:
            max = result[0]

    gap = (max - min)/10

    intervals = [(min, min+gap), (min+gap, min+gap*2), (min+gap*2, min+gap*3), (min+gap*3, min+gap*4), (min+gap*4, min+gap*5), (min+gap*5, min+gap*6), (min+gap*6, min+gap*7), (min+gap*7, min+gap*8), (min+gap*8, min+gap*9), (min+gap*9, max)]
    for result in rv:
        if min <= result[0] and result[0] <= min+gap:
            int0 = int0 + 1
        elif result[0] > min+gap and result[0] <= min+gap*2:
            int1 = int1+1
        elif result[0] > min+gap*2 and result[0] <= min+gap*3:
            int2 = int2 + 1
        elif result[0] > min+gap*3 and result[0] <= min+gap*4:
            int3 = int3 + 1
        elif result[0] > min+gap*4 and result[0] <= min+gap*5:
            int4 = int4 + 1
        elif result[0] > min+gap*5 and result[0] <= min+gap*6:
            int5 = int5 + 1
        elif result[0] > min+gap*6 and result[0] <= min+gap*7:
            int6 = int6 + 1
        elif result[0] > min+gap*7 and result[0] <= min+gap*8:
            int7 = int7 + 1
        elif result[0] > min+gap*8 and result[0] <= min+gap*9:
            int8 = int8 + 1
        elif result[0] > min+gap*9 and result[0] <= max:
            int9 = int9 + 1

    listacont = [int0, int1, int2, int3, int4, int5, int6, int7, int8, int9]

    for obj in zip(intervals, listacont):
        content = {'interval': obj[0], 'totalScore': obj[1]}
        final.append(content)
        content = {}

    return final

def selectHashtagsByFixedIntervals(hashtag, since_date, until_date):
    if since_date=='' or until_date=='':
        if until_date is not '':
            sql = ("SELECT analysis_score FROM datahashtags WHERE hashtag = %s AND date<=%s")
            val = (hashtag, until_date)
            mycursor.execute(sql, val)
        elif since_date is not '':
            sql = ("SELECT analysis_score FROM datahashtags WHERE hashtag = %s AND date>=%s")
            val = (hashtag, since_date)
            mycursor.execute(sql, val)
        else:
            sql = ("SELECT analysis_score FROM datahashtags WHERE hashtag = %s")
            val = (hashtag,)
            mycursor.execute(sql, val)
    else:
        sql = ("SELECT analysis_score FROM datahashtags WHERE hashtag = %s AND date BETWEEN %s AND %s")
        val = (hashtag, since_date, until_date)
        mycursor.execute(sql, val)
    rv = mycursor.fetchall()
    final = []
    content = {}
    int0=0
    int1=0
    int2=0
    int3=0
    int4=0
    int5=0
    int6=0
    int7=0
    int8=0
    int9 = 0

    intervals = [(0,0.1), (0.1,0.2), (0.2,0.3), (0.3,0.4), (0.4,0.5), (0.5,0.6), (0.6,0.7), (0.7,0.8), (0.8,0.9), (0.9,1)]
    for result in rv:
        if 0 <= result[0] and result[0] <= 0.1:
            int0 = int0 + 1
        elif result[0] > 0.1 and result[0] <= 0.2:
            int1 = int1+1
        elif result[0] > 0.2 and result[0] <= 0.3:
            int2 = int2 + 1
        elif result[0] > 0.3 and result[0] <= 0.4:
            int3 = int3 + 1
        elif result[0] > 0.4 and result[0] <= 0.5:
            int4 = int4 + 1
        elif result[0] > 0.5 and result[0] <= 0.6:
            int5 = int5 + 1
        elif result[0] > 0.6 and result[0] <= 0.7:
            int6 = int6 + 1
        elif result[0] > 0.7 and result[0] <= 0.8:
            int7 = int7 + 1
        elif result[0] > 0.8 and result[0] <= 0.9:
            int8 = int8 + 1
        elif result[0] > 0.9 and result[0] <= 1:
            int9 = int9 + 1

    listacont = [int0, int1, int2, int3, int4, int5, int6, int7, int8, int9]

    for obj in zip(intervals, listacont):
        content = {'interval': obj[0], 'totalScore': obj[1]}
        final.append(content)
        content = {}

    return final

def selectHashtagsForPieChart(since_date, until_date):
    if since_date=='' or until_date=='':
        if until_date is not '':
            sql = ("SELECT hashtag, COUNT(*) FROM datahashtags WHERE date<=%s GROUP BY hashtag")
            val = (until_date)
            mycursor.execute(sql, val)
        elif since_date is not '':
            sql = ("SELECT hashtag, COUNT(*) FROM datahashtags WHERE date>=%s GROUP BY hashtag")
            val = (since_date)
            mycursor.execute(sql, val)
        else:
            sql = ("SELECT hashtag, COUNT(*) FROM datahashtags GROUP BY hashtag")
            mycursor.execute(sql)
    else:
        sql = ("SELECT hashtag, COUNT(*) FROM datahashtags WHERE date BETWEEN %s AND %s GROUP BY hashtag")
        val = (since_date, until_date)
        mycursor.execute(sql, val)
    rv = mycursor.fetchall()
    final = []
    content = {}
    for result in rv:
        content = {'hashtags': result[0], 'numero_filas': result[1]}
        final.append(content)
        content = {}
    return final

def select_dataUserTw(user, since_date, until_date):
    if since_date=='' or until_date=='':
        if until_date is not '':
            sql = ("SELECT analysis_score, text, date FROM datausertw WHERE user = %s AND date<=%s")
            val = (user, until_date)
            mycursor.execute(sql, val)
        elif since_date is not '':
            sql = ("SELECT analysis_score, text, date FROM datausertw WHERE user = %s AND date>=%s")
            val = (user, since_date)
            mycursor.execute(sql, val)
        else:
            sql = ("SELECT analysis_score, text, date FROM datausertw WHERE user = %s")
            val = (user,)
            mycursor.execute(sql, val)
    else:
        sql = ("SELECT analysis_score, text, date FROM datausertw WHERE user = %s AND date BETWEEN %s AND %s")
        val = (user, since_date, until_date)
        mycursor.execute(sql, val)
    rv = mycursor.fetchall()
    final = []
    content = {}
    for result in rv:
        content = {'analysis_score': result[0], 'text': result[1], 'date': result[2]}
        final.append(content)
        content = {}
    return final

def selectUserTwGroupByDates(user, since_date, until_date):
    if since_date=='' or until_date=='':
        if until_date is not '':
            sql = ("SELECT AVG(analysis_score), date FROM datausertw WHERE user = %s AND date<=%s GROUP BY date")
            val = (user, until_date)
            mycursor.execute(sql, val)
        elif since_date is not '':
            sql = ("SELECT AVG(analysis_score), date FROM datausertw WHERE user = %s AND date>=%s GROUP BY date")
            val = (user, since_date)
            mycursor.execute(sql, val)
        else:
            sql = ("SELECT AVG(analysis_score), date FROM datausertw WHERE user = %s GROUP BY date")
            val = (user,)
            mycursor.execute(sql, val)
    else:
        sql = ("SELECT AVG(analysis_score), date FROM datausertw WHERE user = %s AND date BETWEEN %s AND %s GROUP BY date")
        val = (user, since_date, until_date)
        mycursor.execute(sql, val)
    rv = mycursor.fetchall()
    final = []
    content = {}
    for result in rv:
        content = {'analysis_score': result[0], 'date': result[1]}
        final.append(content)
        content = {}
    return final

def selectUserTwByIntervals(user, since_date, until_date):
    if since_date=='' or until_date=='':
        if until_date is not '':
            sql = ("SELECT analysis_score FROM datausertw WHERE user = %s AND date<=%s")
            val = (user, until_date)
            mycursor.execute(sql, val)
        elif since_date is not '':
            sql = ("SELECT analysis_score FROM datausertw WHERE user = %s AND date>=%s")
            val = (user, since_date)
            mycursor.execute(sql, val)
        else:
            sql = ("SELECT analysis_score FROM datausertw WHERE user = %s")
            val = (user,)
            mycursor.execute(sql, val)
    else:
        sql = ("SELECT analysis_score FROM datausertw WHERE user = %s AND date BETWEEN %s AND %s")
        val = (user, since_date, until_date)
        mycursor.execute(sql, val)
    rv = mycursor.fetchall()
    final = []
    content = {}
    min = 1
    max = -1
    int0=0
    int1=0
    int2=0
    int3=0
    int4=0
    int5=0
    int6=0
    int7=0
    int8=0
    int9 = 0
    for result in rv:
        if min > result[0]:
            min = result[0]
        if max < result[0]:
            max = result[0]
    gap = (max - min)/10
    intervals = [(min, min+gap), (min+gap, min+gap*2), (min+gap*2, min+gap*3), (min+gap*3, min+gap*4), (min+gap*4, min+gap*5), (min+gap*5, min+gap*6), (min+gap*6, min+gap*7), (min+gap*7, min+gap*8), (min+gap*8, min+gap*9), (min+gap*9, max)]
    for result in rv:
        if min <= result[0] and result[0] <= min+gap:
            int0 = int0 + 1
        elif result[0] > min+gap and result[0] <= min+gap*2:
            int1 = int1+1
        elif result[0] > min+gap*2 and result[0] <= min+gap*3:
            int2 = int2 + 1
        elif result[0] > min+gap*3 and result[0] <= min+gap*4:
            int3 = int3 + 1
        elif result[0] > min+gap*4 and result[0] <= min+gap*5:
            int4 = int4 + 1
        elif result[0] > min+gap*5 and result[0] <= min+gap*6:
            int5 = int5 + 1
        elif result[0] > min+gap*6 and result[0] <= min+gap*7:
            int6 = int6 + 1
        elif result[0] > min+gap*7 and result[0] <= min+gap*8:
            int7 = int7 + 1
        elif result[0] > min+gap*8 and result[0] <= min+gap*9:
            int8 = int8 + 1
        elif result[0] > min+gap*9 and result[0] <= max:
            int9 = int9 + 1
    listacont = [int0, int1, int2, int3, int4, int5, int6, int7, int8, int9]

    for obj in zip(intervals, listacont):
        content = {'interval': obj[0], 'totalScore': obj[1]}
        final.append(content)
        content = {}
    return final

def selectUserTwByFixedIntervals(user, since_date, until_date):
    if since_date=='' or until_date=='':
        if until_date is not '':
            sql = ("SELECT analysis_score FROM datausertw WHERE user = %s AND date<=%s")
            val = (user, until_date)
            mycursor.execute(sql, val)
        elif since_date is not '':
            sql = ("SELECT analysis_score FROM datausertw WHERE user = %s AND date>=%s")
            val = (user, since_date)
            mycursor.execute(sql, val)
        else:
            sql = ("SELECT analysis_score FROM datausertw WHERE user = %s")
            val = (user,)
            mycursor.execute(sql, val)
    else:
        sql = ("SELECT analysis_score FROM datausertw WHERE user = %s AND date BETWEEN %s AND %s")
        val = (user, since_date, until_date)
        mycursor.execute(sql, val)
    rv = mycursor.fetchall()
    final = []
    content = {}
    int0=0
    int1=0
    int2=0
    int3=0
    int4=0
    int5=0
    int6=0
    int7=0
    int8=0
    int9 = 0
    intervals = [(0,0.1), (0.1,0.2), (0.2,0.3), (0.3,0.4), (0.4,0.5), (0.5,0.6), (0.6,0.7), (0.7,0.8), (0.8,0.9), (0.9,1)]
    for result in rv:
        if 0 <= result[0] and result[0] <= 0.1:
            int0 = int0 + 1
        elif result[0] > 0.1 and result[0] <= 0.2:
            int1 = int1+1
        elif result[0] > 0.2 and result[0] <= 0.3:
            int2 = int2 + 1
        elif result[0] > 0.3 and result[0] <= 0.4:
            int3 = int3 + 1
        elif result[0] > 0.4 and result[0] <= 0.5:
            int4 = int4 + 1
        elif result[0] > 0.5 and result[0] <= 0.6:
            int5 = int5 + 1
        elif result[0] > 0.6 and result[0] <= 0.7:
            int6 = int6 + 1
        elif result[0] > 0.7 and result[0] <= 0.8:
            int7 = int7 + 1
        elif result[0] > 0.8 and result[0] <= 0.9:
            int8 = int8 + 1
        elif result[0] > 0.9 and result[0] <= 1:
            int9 = int9 + 1
    listacont = [int0, int1, int2, int3, int4, int5, int6, int7, int8, int9]
    for obj in zip(intervals, listacont):
        content = {'interval': obj[0], 'totalScore': obj[1]}
        final.append(content)
        content = {}
    return final

def select_dataWord(word, since_date, until_date):
    if since_date=='' or until_date=='':
        if until_date is not '':
            sql = ("SELECT analysis_score, text, date FROM dataword WHERE word = %s AND date<=%s")
            val = (word, until_date)
            mycursor.execute(sql, val)
        elif since_date is not '':
            sql = ("SELECT analysis_score, text, date FROM dataword WHERE word = %s AND date>=%s")
            val = (word, since_date)
            mycursor.execute(sql, val)
        else:
            sql = ("SELECT analysis_score, text, date FROM dataword WHERE word = %s")
            val = (word,)
            mycursor.execute(sql, val)
    else:
        sql = ("SELECT analysis_score, text, date FROM dataword WHERE word = %s AND date BETWEEN %s AND %s")
        val = (word, since_date, until_date)
        mycursor.execute(sql, val)
    rv = mycursor.fetchall()
    final = []
    content = {}
    for result in rv:
        content = {'analysis_score': result[0], 'text': result[1], 'date': result[2]}
        final.append(content)
        content = {}
    return final

def selectWordGroupByDates(word, since_date, until_date):
    if since_date=='' or until_date=='':
        if until_date is not '':
            sql = ("SELECT AVG(analysis_score), date FROM dataword WHERE word = %s AND date<=%s GROUP BY date")
            val = (word, until_date)
            mycursor.execute(sql, val)
        elif since_date is not '':
            sql = ("SELECT AVG(analysis_score), date FROM dataword WHERE word = %s AND date>=%s GROUP BY date")
            val = (word, since_date)
            mycursor.execute(sql, val)
        else:
            sql = ("SELECT AVG(analysis_score), date FROM dataword WHERE word = %s GROUP BY date")
            val = (word,)
            mycursor.execute(sql, val)
    else:
        sql = ("SELECT AVG(analysis_score), date FROM dataword WHERE word = %s AND date BETWEEN %s AND %s GROUP BY date")
        val = (word, since_date, until_date)
        mycursor.execute(sql, val)
    rv = mycursor.fetchall()
    final = []
    content = {}
    for result in rv:
        content = {'analysis_score': result[0], 'date': result[1]}
        final.append(content)
        content = {}
    return final

def selectWordByIntervals(word, since_date, until_date):
    if since_date=='' or until_date=='':
        if until_date is not '':
            sql = ("SELECT analysis_score FROM dataword WHERE word = %s AND date<=%s")
            val = (word, until_date)
            mycursor.execute(sql, val)
        elif since_date is not '':
            sql = ("SELECT analysis_score FROM dataword WHERE word = %s AND date>=%s")
            val = (word, since_date)
            mycursor.execute(sql, val)
        else:
            sql = ("SELECT analysis_score FROM dataword WHERE word = %s")
            val = (word,)
            mycursor.execute(sql, val)
    else:
        sql = ("SELECT analysis_score FROM dataword WHERE word = %s AND date BETWEEN %s AND %s")
        val = (word, since_date, until_date)
        mycursor.execute(sql, val)
    rv = mycursor.fetchall()
    final = []
    content = {}
    min = 1
    max = -1
    int0=0
    int1=0
    int2=0
    int3=0
    int4=0
    int5=0
    int6=0
    int7=0
    int8=0
    int9 = 0
    for result in rv:
        if min > result[0]:
            min = result[0]
        if max < result[0]:
            max = result[0]
    gap = (max - min)/10
    intervals = [(min, min+gap), (min+gap, min+gap*2), (min+gap*2, min+gap*3), (min+gap*3, min+gap*4), (min+gap*4, min+gap*5), (min+gap*5, min+gap*6), (min+gap*6, min+gap*7), (min+gap*7, min+gap*8), (min+gap*8, min+gap*9), (min+gap*9, max)]
    for result in rv:
        if min <= result[0] and result[0] <= min+gap:
            int0 = int0 + 1
        elif result[0] > min+gap and result[0] <= min+gap*2:
            int1 = int1+1
        elif result[0] > min+gap*2 and result[0] <= min+gap*3:
            int2 = int2 + 1
        elif result[0] > min+gap*3 and result[0] <= min+gap*4:
            int3 = int3 + 1
        elif result[0] > min+gap*4 and result[0] <= min+gap*5:
            int4 = int4 + 1
        elif result[0] > min+gap*5 and result[0] <= min+gap*6:
            int5 = int5 + 1
        elif result[0] > min+gap*6 and result[0] <= min+gap*7:
            int6 = int6 + 1
        elif result[0] > min+gap*7 and result[0] <= min+gap*8:
            int7 = int7 + 1
        elif result[0] > min+gap*8 and result[0] <= min+gap*9:
            int8 = int8 + 1
        elif result[0] > min+gap*9 and result[0] <= max:
            int9 = int9 + 1
    listacont = [int0, int1, int2, int3, int4, int5, int6, int7, int8, int9]

    for obj in zip(intervals, listacont):
        content = {'interval': obj[0], 'totalScore': obj[1]}
        final.append(content)
        content = {}
    return final

def selectWordByFixedIntervals(word, since_date, until_date):
    if since_date=='' or until_date=='':
        if until_date is not '':
            sql = ("SELECT analysis_score FROM dataword WHERE word = %s AND date<=%s")
            val = (word, until_date)
            mycursor.execute(sql, val)
        elif since_date is not '':
            sql = ("SELECT analysis_score FROM dataword WHERE word = %s AND date>=%s")
            val = (word, since_date)
            mycursor.execute(sql, val)
        else:
            sql = ("SELECT analysis_score FROM dataword WHERE word = %s")
            val = (word,)
            mycursor.execute(sql, val)
    else:
        sql = ("SELECT analysis_score FROM dataword WHERE word = %s AND date BETWEEN %s AND %s")
        val = (word, since_date, until_date)
        mycursor.execute(sql, val)
    rv = mycursor.fetchall()
    final = []
    content = {}
    int0=0
    int1=0
    int2=0
    int3=0
    int4=0
    int5=0
    int6=0
    int7=0
    int8=0
    int9 = 0
    intervals = [(0,0.1), (0.1,0.2), (0.2,0.3), (0.3,0.4), (0.4,0.5), (0.5,0.6), (0.6,0.7), (0.7,0.8), (0.8,0.9), (0.9,1)]
    for result in rv:
        if 0 <= result[0] and result[0] <= 0.1:
            int0 = int0 + 1
        elif result[0] > 0.1 and result[0] <= 0.2:
            int1 = int1+1
        elif result[0] > 0.2 and result[0] <= 0.3:
            int2 = int2 + 1
        elif result[0] > 0.3 and result[0] <= 0.4:
            int3 = int3 + 1
        elif result[0] > 0.4 and result[0] <= 0.5:
            int4 = int4 + 1
        elif result[0] > 0.5 and result[0] <= 0.6:
            int5 = int5 + 1
        elif result[0] > 0.6 and result[0] <= 0.7:
            int6 = int6 + 1
        elif result[0] > 0.7 and result[0] <= 0.8:
            int7 = int7 + 1
        elif result[0] > 0.8 and result[0] <= 0.9:
            int8 = int8 + 1
        elif result[0] > 0.9 and result[0] <= 1:
            int9 = int9 + 1
    listacont = [int0, int1, int2, int3, int4, int5, int6, int7, int8, int9]
    for obj in zip(intervals, listacont):
        content = {'interval': obj[0], 'totalScore': obj[1]}
        final.append(content)
        content = {}
    return final

def select_dataUserIg(user, since_date, until_date):
    if since_date=='' or until_date=='':
        if until_date is not '':
            sql = ("SELECT analysis_score, comment, datepost FROM datauserig WHERE user = %s AND datepost<=%s")
            val = (user, until_date)
            mycursor.execute(sql, val)
        elif since_date is not '':
            sql = ("SELECT analysis_score, comment, datepost FROM datauserig WHERE user = %s AND datepost>=%s")
            val = (user, since_date)
            mycursor.execute(sql, val)
        else:
            sql = ("SELECT analysis_score, comment, datepost FROM datauserig WHERE user = %s")
            val = (user,)
            mycursor.execute(sql, val)
    else:
        sql = ("SELECT analysis_score, comment, datepost FROM datauserig WHERE user = %s AND datepost BETWEEN %s AND %s")
        val = (user, since_date, until_date)
        mycursor.execute(sql, val)
    rv = mycursor.fetchall()
    final = []
    content = {}
    for result in rv:
        content = {'analysis_score': result[0], 'text': result[1], 'date': result[2]}
        final.append(content)
        content = {}
    return final

def selectDataUserIgByDates(user, since_date, until_date):
    if since_date=='' or until_date=='':
        if until_date is not '':
            sql = ("SELECT AVG(analysis_score), datepost FROM datauserig WHERE user = %s AND datepost<=%s GROUP BY datepost")
            val = (user, until_date)
            mycursor.execute(sql, val)
        elif since_date is not '':
            sql = ("SELECT AVG(analysis_score), datepost FROM datauserig WHERE user = %s AND datepost>=%s GROUP BY datepost")
            val = (user, since_date)
            mycursor.execute(sql, val)
        else:
            sql = ("SELECT AVG(analysis_score), datepost FROM datauserig WHERE user = %s GROUP BY datepost")
            val = (user,)
            mycursor.execute(sql, val)
    else:
        sql = ("SELECT AVG(analysis_score), datepost FROM datauserig WHERE user = %s AND datepost BETWEEN %s AND %s GROUP BY datepost")
        val = (user, since_date, until_date)
        mycursor.execute(sql, val)
    rv = mycursor.fetchall()
    final = []
    content = {}
    for result in rv:
        content = {'analysis_score': result[0], 'date': result[1]}
        final.append(content)
        content = {}
    return final

def selectDataUserIgByIntervals(user, since_date, until_date):
    if since_date=='' or until_date=='':
        if until_date is not '':
            sql = ("SELECT analysis_score FROM datauserig WHERE user = %s AND datepost<=%s")
            val = (user, until_date)
            mycursor.execute(sql, val)
        elif since_date is not '':
            sql = ("SELECT analysis_score FROM datauserig WHERE user = %s AND datepost>=%s")
            val = (user, since_date)
            mycursor.execute(sql, val)
        else:
            sql = ("SELECT analysis_score FROM datauserig WHERE user = %s")
            val = (user,)
            mycursor.execute(sql, val)
    else:
        sql = ("SELECT analysis_score FROM datauserig WHERE user = %s AND datepost BETWEEN %s AND %s")
        val = (user, since_date, until_date)
        mycursor.execute(sql, val)
    rv = mycursor.fetchall()
    final = []
    content = {}
    min = 1
    max = -1
    int0=0
    int1=0
    int2=0
    int3=0
    int4=0
    int5=0
    int6=0
    int7=0
    int8=0
    int9 = 0
    for result in rv:
        if min > result[0]:
            min = result[0]
        if max < result[0]:
            max = result[0]
    gap = (max - min)/10
    intervals = [(min, min+gap), (min+gap, min+gap*2), (min+gap*2, min+gap*3), (min+gap*3, min+gap*4), (min+gap*4, min+gap*5), (min+gap*5, min+gap*6), (min+gap*6, min+gap*7), (min+gap*7, min+gap*8), (min+gap*8, min+gap*9), (min+gap*9, max)]
    for result in rv:
        if min <= result[0] and result[0] <= min+gap:
            int0 = int0 + 1
        elif result[0] > min+gap and result[0] <= min+gap*2:
            int1 = int1+1
        elif result[0] > min+gap*2 and result[0] <= min+gap*3:
            int2 = int2 + 1
        elif result[0] > min+gap*3 and result[0] <= min+gap*4:
            int3 = int3 + 1
        elif result[0] > min+gap*4 and result[0] <= min+gap*5:
            int4 = int4 + 1
        elif result[0] > min+gap*5 and result[0] <= min+gap*6:
            int5 = int5 + 1
        elif result[0] > min+gap*6 and result[0] <= min+gap*7:
            int6 = int6 + 1
        elif result[0] > min+gap*7 and result[0] <= min+gap*8:
            int7 = int7 + 1
        elif result[0] > min+gap*8 and result[0] <= min+gap*9:
            int8 = int8 + 1
        elif result[0] > min+gap*9 and result[0] <= max:
            int9 = int9 + 1
    listacont = [int0, int1, int2, int3, int4, int5, int6, int7, int8, int9]

    for obj in zip(intervals, listacont):
        content = {'interval': obj[0], 'totalScore': obj[1]}
        final.append(content)
        content = {}
    return final

def selectDataUserIgByFixedIntervals(user, since_date, until_date):
    if since_date=='' or until_date=='':
        if until_date is not '':
            sql = ("SELECT analysis_score FROM datauserig WHERE user = %s AND datepost<=%s")
            val = (user, until_date)
            mycursor.execute(sql, val)
        elif since_date is not '':
            sql = ("SELECT analysis_score FROM datauserig WHERE user = %s AND datepost>=%s")
            val = (user, since_date)
            mycursor.execute(sql, val)
        else:
            sql = ("SELECT analysis_score FROM datauserig WHERE user = %s")
            val = (user,)
            mycursor.execute(sql, val)
    else:
        sql = ("SELECT analysis_score FROM datauserig WHERE user = %s AND datepost BETWEEN %s AND %s")
        val = (user, since_date, until_date)
        mycursor.execute(sql, val)
    rv = mycursor.fetchall()
    final = []
    content = {}
    int0=0
    int1=0
    int2=0
    int3=0
    int4=0
    int5=0
    int6=0
    int7=0
    int8=0
    int9 = 0
    intervals = [(0,0.1), (0.1,0.2), (0.2,0.3), (0.3,0.4), (0.4,0.5), (0.5,0.6), (0.6,0.7), (0.7,0.8), (0.8,0.9), (0.9,1)]
    for result in rv:
        if 0 <= result[0] and result[0] <= 0.1:
            int0 = int0 + 1
        elif result[0] > 0.1 and result[0] <= 0.2:
            int1 = int1+1
        elif result[0] > 0.2 and result[0] <= 0.3:
            int2 = int2 + 1
        elif result[0] > 0.3 and result[0] <= 0.4:
            int3 = int3 + 1
        elif result[0] > 0.4 and result[0] <= 0.5:
            int4 = int4 + 1
        elif result[0] > 0.5 and result[0] <= 0.6:
            int5 = int5 + 1
        elif result[0] > 0.6 and result[0] <= 0.7:
            int6 = int6 + 1
        elif result[0] > 0.7 and result[0] <= 0.8:
            int7 = int7 + 1
        elif result[0] > 0.8 and result[0] <= 0.9:
            int8 = int8 + 1
        elif result[0] > 0.9 and result[0] <= 1:
            int9 = int9 + 1
    listacont = [int0, int1, int2, int3, int4, int5, int6, int7, int8, int9]
    for obj in zip(intervals, listacont):
        content = {'interval': obj[0], 'totalScore': obj[1]}
        final.append(content)
        content = {}
    return final

def select_statistics(id):
    sql = ("SELECT * FROM statistics WHERE id = %s")
    val = (id,)
    mycursor.execute(sql, val)
    result = mycursor.fetchall()
    return result
