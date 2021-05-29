from flask import Flask, render_template, escape, request, send_from_directory, url_for
import sqlite3

app = Flask(__name__)

@app.route("/")
def top():
    return render_template("top.html")

@app.route("/hoge", methods = ["POST"])
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
        return render_template("error.html")

    con = sqlite3.connect("./data.db")
    cur = con.cursor()
    former_log = list(cur.execute("select * from Log where person=? order by date_time;", (id_num)))
    member = list(cur.execute("select name from where id=? Member;"), (id_num))

    if id_num not in [row["id"] for row in member]:
        return render_template("error.html")
    
    status_register = None
    if former_log[-1]["status"] == "in":
        status_register = "out"
    elif former_log[-1]["status"] == "out":
        status_register = "in"
    else:
        # status not defined
        return render_template("error.html")
    
    sql_register = "insert into Log(status, person) values(?, ?);"
    cur.execute(sql_register, (status_register, id_num))

    return render_template("success.html",status=status_register,name=member[0]["name"])

if __name__ == "__main__":
    app.run()