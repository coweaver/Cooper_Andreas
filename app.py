from flask import Flask, render_template, request
from utils import dbmanager


app=Flask(__name__)

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method=="GET":
        return render_template("login.html")
    else:
        email = request.form["usermail"]
        pword = request.form["pword"]
        valid = dbmanager.authenticate(email,pword)
        if not(valid):
            return render_template("login.html")
        else:
            name = dbmanager.getName(email)
            return render_template(Home.html,name=name)

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method=="GET":
        return render_template("register.html")
    else:
        email = request.form["usermail"]
        pword = request.form["pword"]
        name = request.form["name"]
        valid_email = dbmanager.checkEmail(email)
        if not(valid_email):
            error = "Email Already Exists"
            return render_template("register.html", error=error)
