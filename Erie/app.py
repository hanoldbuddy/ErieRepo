"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask, render_template
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
# wsgi_app = app.wsgi_app


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

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
