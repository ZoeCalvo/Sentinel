from flask import Flask, jsonify, redirect, url_for, request
from flask_cors import CORS
import mysql.connector
import os
import json
from src.instagram import *
from src.twitter import *

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

@app.route('/twitter')
def init_tw():
    print("Selecciona una opción")
    print("1. Buscar tweets en un hashtag")
    print("2. Buscar tweets donde aparezca un usuario mencionado")
    print("3. Buscar tweets relacionados con una palabra")

    option = input("Introduce el número de la opción deseada: ")

    if option == "1":
        hashtag = input("Introduzca el hashtag con #: ")
        since_date = input("Introduce la fecha de comienzo de búsqueda: ")
        until_date = input("Introduce la fecha de fin de búsqueda: ")
        analysis_score_hashtag = searchHashtag(hashtag, since_date, until_date)
        results_analysis_json = json.dumps(analysis_score_hashtag)

        return jsonify({'results_analysis' : results_analysis_json})

    if option == "2":
        user = input("Introduzca el nombre del usuario con @: ")
        since_date = input("Introduce la fecha de comienzo de búsqueda: ")
        until_date = input("Introduce la fecha de fin de búsqueda: ")
        analysis_score_user =  searchUser(user, since_date, until_date)
        results_analysis_json = json.dumps(analysis_score_user)

        return jsonify({'results_analysis' : results_analysis_json})

    if option == "3":
        word = input("Introduce la palabra: ")
        since_date = input("Introduce la fecha de comienzo de búsqueda: ")
        until_date = input("Introduce la fecha de fin de búsqueda: ")
        analysis_score_word = searchWord(word, since_date, until_date)
        results_analysis_json = json.dumps(analysis_score_word)
        return jsonify({'results_analysis': results_analysis_json})


if __name__ == '__main__':
    app.run()

