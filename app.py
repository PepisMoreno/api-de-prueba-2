from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")
    #agrego lo que tenía la pagina que me mandó cari
    if __name__=="__main__":
        app.run()


