from app import app
from flask import render_template

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/about")
def about():
    return render_template("about/about.html")
@app.route("/piano")
def piano():
    return render_template("piano/piano.html")
@app.route("/ham")
def ham():
    return render_template("ham/ham.html")
@app.route("/eng")
def eng():
    return render_template("eng/eng.html")
@app.route("/drone")
def drone():
    return render_template("drone/drone.html")
@app.route("/contact")
def contact():
    return render_template("contact/contact.html")
@app.route("/ai")
def ai():
    return render_template("ai/ai.html")

# Code for the masses

@app.route("")
