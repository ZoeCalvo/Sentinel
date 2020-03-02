from flask import Flask, jsonify, render_template
from flask_cors import CORS
import mysql.connector
import os
# import src.instagram
import json
from src.instagram import *

# from src.twitter import *

app = Flask(__name__)
CORS(app)

user_db = os.getenv('USER_DB')
pass_db = os.getenv('PASSWD_DB')
mydb = mysql.connector.connect(host="localhost", user=user_db, passwd=pass_db, database="telusko")

mycursor = mydb.cursor()


def insertarEnBD():
    sql = "INSERT INTO student(name , college) VALUES(%s,%s)"
    val = ("Maria", "rist")
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")


@app.route('/')
def titulo():

    return jsonify({'text': 'Hola!!!'})


@app.route('/instagram')
def init_ig():
    api_ig = main()
    user = input("Introduce tu nombre de usuario sin @: ")
    userId = search_users(api_ig, user)
    userId_json = json.dumps(userId)
    return jsonify({'userID' : userId_json})



if __name__ == '__main__':
    app.run()

