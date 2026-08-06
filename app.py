from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# PostgreSQL Database
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# ---------------- DATABASE TABLE ----------------
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    message = db.Column(db.Text)


# Create table automatically
with app.app_context():
    db.create_all()


# ---------------- HOME ----------------
@app.route("/")
def home():
    return render_template("index.html")


# ---------------- CONTACT ----------------
@app.route("/contact", methods=["POST"])
def contact():

    new_contact = Contact(
        name=request.form["name"],
        email=request.form["email"],
        message=request.form["message"]
    )

    db.session.add(new_contact)
    db.session.commit()

    return """
    <html>
    <head>
    <title>Success</title>
    <style>
    body{
        background:#0f172a;
        color:white;
        font-family:Arial;
        text-align:center;
        padding-top:120px;
    }
    a{
        color:#38bdf8;
        text-decoration:none;
        font-size:20px;
    }
    </style>
    </head>

    <body>

    <h1>✅ Thank You!</h1>

    <h2>Your message has been submitted successfully.</h2>

    <br>

    <a href="/">⬅ Back to Portfolio</a>

    </body>
    </html>
    """


# ---------------- ADMIN ----------------
@app.route("/admin")
def admin():

    messages = Contact.query.order_by(Contact.id.desc()).all()

    return render_template("admin.html", messages=messages)


# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(debug=True)