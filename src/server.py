from flask import Flask, jsonify, redirect, url_for, request
from flask_cors import CORS
import mysql.connector
import os
import json
from src.instagram import *

# from src.twitter import *

app = Flask(__name__)
CORS(app)

user_db = os.getenv('USER_DB')
pass_db = os.getenv('PASSWD_DB')
mydb = mysql.connector.connect(host="localhost", user=user_db, passwd=pass_db, database="telusko")

mycursor = mydb.cursor()

@app.route('/register', methods=['POST'])
def insertarEnBD():

    sql = ("INSERT INTO register(name, surname, user, passwd) VALUES(%s,%s, %s, %s)")
    data = request.json
    name=data.get('name')
    surname = data.get('surname')
    username = data.get('user')
    passwd = data.get('passwd')
    val = (name, surname, username, passwd)
    mycursor.execute(sql, val)
    mydb.commit()
    #print(mycursor.rowcount, "record inserted.")
    return 'OK'

@app.route('/')
def titulo():

    return jsonify({'text': 'Hola!!!'})


@app.route('/instagram')
def init_ig():
    api_ig = main()
    followings = input("¿Quieres mirar a quién sigues?: (Y/N) ")
    if followings == "Y":
        user = input("Introduce tu nombre de usuario sin @: ")
        userId = search_users(api_ig, user)
        research(api_ig, userId)
    else:
        ans = input("Quieres buscar a un usuario concreto?: (Y/N) ")
        if ans == "Y":
            user = input("Introduce el nombre del usuario sin @: ")
            userId = search_users(api_ig, user)
            results_analysis = getMediaData(api_ig, userId)
            userId_json = json.dumps(userId)
            results_analysis_json = json.dumps(results_analysis)
        else:
            explore(api_ig)

    return jsonify({'userID' : userId_json, 'results_analysis' : results_analysis_json})



if __name__ == '__main__':
    app.run()

