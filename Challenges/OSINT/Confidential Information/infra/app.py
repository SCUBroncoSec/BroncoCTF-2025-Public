import os
from flask import Flask, redirect, render_template, request, session, url_for
from utils import validate_security_questions, validate_user


app = Flask(__name__)
app.secret_key = "your secret key"

FLAG = "bronco{n0t_s0_s3cur3_n0w_s1m0n!}"

@app.route("/", methods=["GET", "POST"])
def login():
    msg = ""
    if request.method == "POST" and "username" in request.form and "password" in request.form:
        username = request.form["username"]
        password = request.form["password"]

        if validate_user(username, password):
            # Create session data, we can access this data in other routes
            session["loggedin"] = True
            session["username"] = username

            # Redirect to flag page
            return render_template("flag.html", flag=FLAG)
        else:
            # Account doesnt exist or username/password incorrect
            msg = f'Incorrect username/password'

    return render_template("index.html", msg=msg)

@app.route("/forgot-password", methods=["GET", "POST"])
def questions():
    msg = ""
    if request.method == "POST" and "username" in request.form and "q1" in request.form and "q2" in request.form and "q3" in request.form:
        username = request.form["username"]
        q1 = request.form["q1"].lower()
        q2 = request.form["q2"].lower()
        q3 = request.form["q3"].lower()

        if validate_security_questions(username, q1, q2, q3):
            session["loggedin"] = True
            session["username"] = username

            #return redirect(url_for("flag"))
            return render_template("flag.html", flag=FLAG)
        else:
            msg = "Incorrect username/security questions"
    return render_template("questions.html", msg=msg)


@app.route("/logout")
def logout():
    # Remove session data, this will log the user out
    session.pop("loggedin", None)
    session.pop("username", None)
    # Redirect to login page
    return redirect(url_for("login"))


@app.route("/flag")
def flag():
    # Check if user is loggedin
    if "loggedin" in session:
        # User is loggedin show them the flag page
        return render_template("flag.html", username=session["username"])

    # User is not loggedin redirect to login page
    return redirect(url_for("login"))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 80))
    app.run(debug=False, host="0.0.0.0", port=port)
