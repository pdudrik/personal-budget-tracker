from flask import url_for, render_template
from app import app



@app.route("/index", methods=["GET"])
@app.route("/home", methods=["GET"])
@app.route("/", methods=["GET"])
def home_route():
    return render_template("home.html", title="Home Page", heading="HOME")


@app.route("/income", methods=["GET"])
def income_route():
    return render_template("income.html", title="Income Page", heading="INCOME")


@app.route("/expenses", methods=["GET"])
def expenses_route():
    return render_template("expenses.html", title="Expenses page", heading="EXPENSES")
