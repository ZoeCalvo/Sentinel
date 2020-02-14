from flask import Flask, render_template
import mysql.connector
from claves import *
app = Flask(__name__)

mydb = mysql.connector.connect(host="localhost", user=user_bd, passwd=pass_bd, database="telusko")

mycursor = mydb.cursor()


def insertarEnBD():
    sql = "INSERT INTO student(name , college) VALUES(%s,%s)"
    val = ("Maria", "rist")
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")


@app.route('/')
def titulo():
    title = "Sentinel"
    user = {'nombre': 'Zoe'}

    return render_template("plantilla.html", title=title, user=user)

if __name__ == '__main__':
    app.run()

