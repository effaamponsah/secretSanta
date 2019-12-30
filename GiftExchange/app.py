from flask import Flask, render_template, Response
import csv
import sqlite3 as sql


app = Flask(__name__)


@app.route("/")
def index():
    return render_template(
        "index.html"
    )


if __name__ == "__main__":
    app.run(debug=True, port=8000)
