import csv
from flask import Flask, render_template, flash, request
from flask_bootstrap import Bootstrap
from datetime import datetime
from dotenv import load_dotenv, dotenv_values
import os

config = dotenv_values(".env")

app = Flask(__name__)
app.config['SECRET_KEY'] = config["SECRET_KEY"]
Bootstrap(app)
year = datetime.now().year


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        guest_name = request.form['name']
        guest_email = request.form['email']
        guest_msg = request.form['message']
        flash('you\'ve successfully sent a message! ')
        with open(config["PATH"], mode='a') as f:
            writer = csv.writer(f)
            writer.writerow([guest_name, guest_email, guest_msg])
        return render_template("index.html", year=year, name=guest_name)
    return render_template("index.html", year=year)


if __name__ == "__main__":
    app.run(debug=bool(config["DEBUG_MODE"]))
