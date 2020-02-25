from flask import Flask, render_template
import mysql.connector
import os

app = Flask(__name__)
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
    title = "Sentinel"
    user = {'nombre': 'Zoe'}

    return render_template("plantilla.html", title=title, user=user)

if __name__ == '__main__':
    app.run()

