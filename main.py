import csv
from flask import Flask, render_template, flash, request
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from datetime import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hjhbjghkljkvhgv657656v'
ckeditor = CKEditor(app)
Bootstrap(app)

year = datetime.now().year


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        guest_name = request.form['name']
        guest_email = request.form['email']
        guest_msg = request.form['message']
        flash('you\'ve successfully sent a message! ')
        with open('guest_data.csv', mode='a') as f:
            writer = csv.writer(f)
            writer.writerow([guest_name, guest_email, guest_msg])
        return render_template("index.html", year=year, name=guest_name)
    return render_template("index.html", year=year)


if __name__ == "__main__":
    app.run(debug=True)
