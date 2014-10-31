from flask import Flask, render_template, request, redirect, url_for
from dbmanager import *


app=Flask(__name__)

@app.route("/", methods=["GET","POST"])
@app.route("/login", methods=["GET","POST"])
def login():
    print_Everything()
    if request.method=="GET":
        return render_template("login.html")
    else:
        email = request.form["usermail"]
        pword = request.form["pword"]
        valid = authenticate(email,pword)
        if not(valid):
            return render_template("login.html", error="Not a valid Email or Password")
        else:
            name = getName(email)
            return render_template("home.html",name=name)


@app.route("/register", methods=["GET","POST"])
def register():
    if request.method=="GET":
        return render_template("register.html")
    else:
        email = request.form["usermail"]
        pword = request.form["pword"]
        name = request.form["name"]
        valid_email = not checkEmail(email)
        if not(valid_email):
            error = "Email Already Exists"
            return render_template("register.html", error=error)
        add(name,email,pword)
        return redirect(url_for("/login"))



if __name__=="__main__":
    app.debug=True
    app.run()
