from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")
    #agrego lo que tenía la pagina que me mandó cari
    if __name__=="__main__":
        app.run()


#request sirve para recolectar la data que viene del formulario
