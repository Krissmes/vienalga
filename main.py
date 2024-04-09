from flask import Flask, render_template, request
from dati import dabut_rindinas, pierakstit_klat

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/teksts")
def te():
    return render_template("teksts.html")

@app.route("/saraksts")
def saraksts():
    saraksts = ["Anna", "Katls", "Kartupelis"]
    bildes = ["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRcCG4898FTkK5IUBMpLleBHtjK3jUILS3YsjCFfLr56g&s","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQtv-3G97RDAt-sgNqxhaEB4f2SDwVxJaOq7JOY0D_7zA&s","https://www.darzaabc.lv/public/assets/images/products/Agrimatco/kartupe%C4%BCi/kartupeli-monalisa-dzeltenie-seklas-kartupelu-stadamais-materials.jpg"]
    kopejais_saraksts = []
    faila_rindas = dabut_rindinas()
    for rinda in faila_rindas:
        elements = rinda.split(", ")
        kopejais_saraksts.append(elements)

    return render_template("saraksts.html", vardi = saraksts, bildes = bildes, garums = len(saraksts), visi = kopejais_saraksts)

@app.route("/info", methods=['POST', 'GET'])
def info():
    if request.method == "POST":
        nosaukums = request.form["nosaukums"]
        adrese = request.form["adrese"]
        rinda = nosaukums + ", " + adrese
        pierakstit_klat(rinda)
    return render_template("info.html")


if __name__ == '__main__':
    app.run(port = 5000)

print("Sveiki!")