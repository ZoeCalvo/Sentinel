from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def titulo():
    title = "Sentinel"
    user = {'nombre': 'Zoe'}

    return render_template("plantilla.html", title=title, user=user)

if __name__ == '__main__':
    app.run()
