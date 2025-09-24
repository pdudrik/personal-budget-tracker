from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from app.config import SECRET_KEY, SQLITE_PATH, CATEGORY_LABELS


app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{SQLITE_PATH}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False        # suppress the error on boot
# app.jinja_env.globals["CATEGORY_LABELS"] = CATEGORY_LABELS
CSRFProtect(app)

db = SQLAlchemy(app)

from app import routes