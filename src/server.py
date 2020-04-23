from flask import Flask, jsonify, redirect, url_for, request
from flask_cors import CORS
import mysql.connector
import os
import json
from src.instagram import *
from src.twitter import *
from src.database import *

app = Flask(__name__)
CORS(app)



@app.route('/login', methods=['POST'])
def login():
    result = get_user(request.json)
    return jsonify({'resultado': result})

@app.route('/register', methods=['POST'])
def register_db():
    register_users(request.json)
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
            results_analysis = getMediaData(api_ig, userId, user)
            userId_json = json.dumps(userId)
            results_analysis_json = json.dumps(results_analysis)
        else:
            explore(api_ig)

    return jsonify({'userID' : userId_json, 'results_analysis' : results_analysis_json})

@app.route('/twitter', methods=['POST'])
def init_tw():
    is_tw = True
    # print(request.json)


    # intermediate(request.json.get('id'), is_tw)
    return jsonify('ok')


    # option = input("Introduce el número de la opción deseada: ")
    #
    # if option == "1":
    #     hashtag = input("Introduzca el hashtag con #: ")
    #     since_date = input("Introduce la fecha de comienzo de búsqueda: ")
    #     until_date = input("Introduce la fecha de fin de búsqueda: ")
    #     analysis_score_hashtag = searchHashtag(hashtag, since_date, until_date)
    #     results_analysis_json = json.dumps(analysis_score_hashtag)
    #
    #     return jsonify({'results_analysis' : results_analysis_json})
    #
    # if option == "2":
    #     user = input("Introduzca el nombre del usuario con @: ")
    #     since_date = input("Introduce la fecha de comienzo de búsqueda: ")
    #     until_date = input("Introduce la fecha de fin de búsqueda: ")
    #     analysis_score_user =  searchUser(user, since_date, until_date)
    #     results_analysis_json = json.dumps(analysis_score_user)
    #
    #     return jsonify({'results_analysis' : results_analysis_json})
    #
    # if option == "3":
    #     word = input("Introduce la palabra: ")
    #     since_date = input("Introduce la fecha de comienzo de búsqueda: ")
    #     until_date = input("Introduce la fecha de fin de búsqueda: ")
    #     analysis_score_word = searchWord(word, since_date, until_date)
    #     results_analysis_json = json.dumps(analysis_score_word)
    #     return jsonify({'results_analysis': results_analysis_json})


@app.route('/getDataforDashboard', methods=['GET'])
def getDataforDashboard():

    # if is_tw == True:
    #     if id[0] == '#':
    analysis_score = select_dataHashtags(request.args.get('id'))
    #     elif id[0] == '@':
    #         analysis_score = select_dataUserTw(id)
    #     else:
    #         analysis_score = select_dataWord(id)
    # else:
    #     analysis_score = select_dataUserIg(id)

    return jsonify({'data':analysis_score})

if __name__ == '__main__':
    app.run()

