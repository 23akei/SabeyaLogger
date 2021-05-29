from flask import Flask, render_template, escape, request, send_from_directory, url_for
import sqlite3

app = Flask(__name__)

@app.route("/")
def top():
    return render_template("top.html")

@app.route(methods = ["POST"])
def record():
    id_num = 0
    
    if request.method == None:
        return render_template("error.html")
    
    id_input = str(request.form["id"])
    if(len(id_input) == 9):
        id_num = int(id_input)
    elif(len(id_input) == 13):
        id_num = int(id_input[3:11])
    else:
        return render_template("error_input.html")

    con = sqlite3.connect("./data.db")
    cur = con.cursor()
    sql = "select * from log;"
    former_log = list(cur.execute(sql))

    

if __name__ == "__main__":
    app.run()