from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)

# MySQL Connection
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",   # XAMPP default password blank hota hai
    database="portfolio_db"
)


# ---------------- HOME ----------------
@app.route("/")
def home():
    return render_template("index.html")


# ---------------- CONTACT FORM ----------------
@app.route("/contact", methods=["POST"])
def contact():

    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]

    cursor = connection.cursor()

    sql = """
    INSERT INTO contact(name, email, message)
    VALUES (%s, %s, %s)
    """

    cursor.execute(sql, (name, email, message))
    connection.commit()

    cursor.close()

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

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM contact ORDER BY id DESC")

    messages = cursor.fetchall()

    cursor.close()

    return render_template("admin.html", messages=messages)


# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(debug=True)