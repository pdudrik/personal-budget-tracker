from flask import url_for, render_template, redirect, request, jsonify
from app import app
from app.db_handler import get_all_income_records, add_income_record, \
    delete_income_record, update_income_record, get_all_expenses_records, \
    add_expenses_record, update_expenses_record, delete_expenses_record
from app.forms import IncomeForm, ExpensesForm



@app.route("/index", methods=["GET"])
@app.route("/home", methods=["GET"])
@app.route("/", methods=["GET"])
def home_route():
    return render_template("home.html", title="Home Page", heading="HOME")


################### INCOME PAGE ###################
@app.route("/income", methods=["GET"])
def income_route():
    form = IncomeForm()

    if request.method == "GET":
        data = get_all_income_records()
            
        return render_template("income.html", title="Income Page",
                               heading="INCOME", context=data, form=form)


@app.route("/income/new", methods=["POST"])
def add_income_record_route():
    form = IncomeForm()
    if form.validate_on_submit():
        if form.submit.data:
            print(f"SUBMIT: {form.submit.data}")
            add_income_record(ammount=form.ammount.data,
                                source=form.source.data,
                                ts=form.ts.data,
                                note=form.note.data)
        
        # Handle error
        else:
            pass
    
    return redirect(url_for("income_route"))


@app.route("/income/<int:recordId>/update", methods=["POST"])
def update_income_record_route(recordId):
    form = IncomeForm()
    if form.validate_on_submit():
        if form.update.data:
            update_income_record(recordId, ammount=form.ammount.data,
                                 source=form.source.data,
                                 ts=form.ts.data, note=form.note.data)
            print(f"record ID: {recordId}")

            # Handle error
        else:
            pass
    
    return redirect(url_for("income_route"))


@app.route("/income/delete-record", methods=["POST"])
def delete_income_route():
    if request.method == "POST":
        recordId = request.get_json()["recordId"]
        delete_income_record(recordId)

        return jsonify({"success": True})
    

################### EXPENSES PAGE ###################
@app.route("/expenses", methods=["GET"])
def expenses_route():
        form = ExpensesForm()

        if request.method == "GET":
            data = get_all_expenses_records()
            
            return render_template("expenses.html", title="Expeness Page",
                                   heading="EXPENSES", context=data, form=form)


@app.route("/expenses/new", methods=["POST"])
def add_expenses_record_route():
    form = ExpensesForm()
    if form.validate_on_submit():
        if form.submit.data:
            print(f"SUBMIT: {form.submit.data}")
            add_expenses_record(ammount=form.ammount.data,
                                category=form.category.data,
                                subcategory=form.subcategory.data,
                                ts=form.ts.data,
                                note=form.note.data)
        
        # Handle error
        else:
            pass
    
    return redirect(url_for("expenses_route"))


@app.route("/expenses/<int:recordId>/update", methods=["POST"])
def update_expenses_record_route(recordId):
    form = ExpensesForm()
    if form.validate_on_submit():
        if form.update.data:
            update_expenses_record(recordId,
                                   ammount=form.ammount.data,
                                   category=form.category.data,
                                   subcategory=form.subcategory.data,
                                   ts=form.ts.data,
                                   note=form.note.data)
            print(f"record ID: {recordId}")

        # Handle error
        else:
            pass
    
    return redirect(url_for("expenses_route"))


@app.route("/expenses/delete-record", methods=["POST"])
def delete_expenses_route():
    if request.method == "POST":
        recordId = request.get_json()["recordId"]
        delete_expenses_record(recordId)

        return jsonify({"success": True})



################### GOALS PAGE ###################
@app.route("/goals", methods=["GET"])
def goals_route():
    return render_template("goals.html", title="Goals page", heading="GOALS")
