from flask import Flask, render_template, flash, request
from flask_bootstrap import Bootstrap
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv('.envvar')
dotenv_path = os.path.join
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", 'default_value')

Bootstrap(app)
year = datetime.now().year


##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL", "sqlite:///guest.db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "guest-data"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=False, nullable=False)
    message = db.Column(db.String(1000))

db.create_all()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        flash('you\'ve successfully sent a message! ')
        new_user = User(
            name=request.form['name'],
            email=request.form['email'],
            message=request.form['message'],
        )
        db.session.add(new_user)
        db.session.commit()
        return render_template("index.html", year=year, name=request.form['name'])
    return render_template("index.html", year=year)


if __name__ == "__main__":
    app.run(debug=bool(os.getenv("DEBUG_MODE")))
