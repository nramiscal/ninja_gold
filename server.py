from flask import Flask, render_template, request, redirect, session
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key = "secret"

@app.route("/")
def index():
    if "total_gold" not in session:
        session["total_gold"] = 0
    if "activities" not in session:
        session["activities"] = []
    return render_template("index.html")

@app.route("/process_money", methods=["POST"])
def process_money():

    if request.form["location"] == "farm":
        gold = random.randint(10,20)
    if request.form["location"] == "cave":
        gold = random.randint(5,10)
    if request.form["location"] == "house":
        gold = random.randint(2,5)
    if request.form["location"] == "casino":
        gold = random.randint(-50,50)

    session["total_gold"] += gold
    now = datetime.now()

    if gold < 0:
        message = f"Entered a {request.form['location']} and lost {-1*gold} golds!...Ouch... ({now})"
        color = "red"
    else:
        message = f"Earned {gold} golds from the {request.form['location']}! ({now})"
        color = "green"


    activity = {
        'message': message,
        'color': color
    }

    session["activities"].append(activity)

    return redirect("/")

@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")


app.run(debug=True)
