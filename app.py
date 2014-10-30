from flask import Flask, render_template, request
from dbmanager import *


app=Flask(__name__)

@app.route("/", methods=["GET","POST"])
@app.route("/login", methods=["GET","POST"])
def login():
    if request.method=="GET":
        return render_template("login.html")
    else:
        email = request.form["usermail"]
        pword = request.form["pword"]
        valid = authenticate(email,pword)
        if not(valid):
            return render_template("login.html")
        else:
            name = getName(email)
            return render_template(Home.html,name=name)


@app.route("/register", methods=["GET","POST"])
def register():
    if request.method=="GET":
        return render_template("register.html")
    else:
        email = request.form["usermail"]
        pword = request.form["pword"]
        name = request.form["name"]
        valid_email = checkEmail(email)
        if not(valid_email):
            error = "Email Already Exists"
            return render_template("register.html", error=error)



if __name__=="__main__":
    app.debug=True
    app.run()
