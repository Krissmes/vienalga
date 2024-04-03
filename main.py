from flask import Flask, render_template

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
    kopejais_saraksts = [["Anna","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRcCG4898FTkK5IUBMpLleBHtjK3jUILS3YsjCFfLr56g&s"], ["Katls", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQtv-3G97RDAt-sgNqxhaEB4f2SDwVxJaOq7JOY0D_7zA&s"], ["Kartupelis", "https://www.darzaabc.lv/public/assets/images/products/Agrimatco/kartupe%C4%BCi/kartupeli-monalisa-dzeltenie-seklas-kartupelu-stadamais-materials.jpg"], ["Mašīna", "https://lh6.googleusercontent.com/Bs8IK7AzA7HDKeel06gttMMDPDoPNzBQdxUTgoKnnFpWhw8tDn8OUWeaaOZeIDnuujmOiEhPBlbDbkjSHKZb-EWByLlqgJCmkF-V-cRau3hEyNqGD-uWqrXEXxnSpvgxj8300Al7"]]
    return render_template("saraksts.html", vardi = saraksts, bildes = bildes, garums = len(saraksts), visi = kopejais_saraksts)


if __name__ == '__main__':
    app.run(port = 5000)

print("Sveiki!")