from app import db
from app.models import Income, Expense, Goal


################### INCOME ###################
def get_all_income_records():
    incomeRecords = Income.query.all()
    outputData = []
    for record in incomeRecords:
        outputData.append({
            "id": record._id,
            "source": record.source,
            "ammount": record.ammount,
            "currency": record.currency,
            "ts": record.ts.strftime("%d.%m.%Y"),
            "note": record.note,
        })
        # print(type(record.note))
    
    return outputData


def add_income_record(ammount, source, ts, note=None):
    income = Income(ammount=ammount, source=source, note=note, ts=ts)
    db.session.add(income)
    db.session.commit()


def update_income_record(recordId, **kwargs):
    incomeRecord = Income.query.filter_by(_id=recordId).first()
    if incomeRecord is None:
        print(f"Record with ID={recordId} not found")
        return
    
    if "ammount" in kwargs:
        incomeRecord.ammount = kwargs["ammount"]
    if "source" in kwargs:
        incomeRecord.source = kwargs["source"]
    if "note" in kwargs:
        incomeRecord.note = kwargs["note"]
    if "ts" in kwargs:
        incomeRecord.ts = kwargs["ts"]

    print(incomeRecord.ammount)
    print(incomeRecord.source)
    print(incomeRecord.note)
    print(incomeRecord.ts)

    db.session.commit()


def delete_income_record(recordId):
    incomeRecord = Income.query.filter_by(_id=recordId).first()
    if incomeRecord is None:
        print(f"Income record with ID={recordId} not found")
        return
        
    db.session.delete(incomeRecord)
    db.session.commit()


################### EXPENSES ###################
def get_all_expenses_records():
    expensesRecrods = Expense.query.all()
    outputData = []
    for record in expensesRecrods:
        outputData.append({
            "id": record._id,
            "ammount": record.ammount,
            "currency": record.currency,
            "ts": record.ts.strftime("%d.%m.%Y"),
            "category": record.category,
            "subcategory": record.subcategory,
            "note": record.note,
        })
    
    return outputData


def add_expenses_record(ammount, category, subcategory, ts, goalFK=None, note=None):
    expense = Expense(ammount=ammount, category=category, subcategory=subcategory,
                      FK_expense_goal=goalFK, note=note, ts=ts)
    db.session.add(expense)
    db.session.commit()


def update_expenses_record(recordId, **kwargs):
    expenseRecord = Expense.query.filter_by(_id=recordId).first()
    if expenseRecord is None:
        print(f"Expense record with ID={recordId} not found")
        return
    
    if "ammount" in kwargs:
        expenseRecord.ammount = kwargs["ammount"]
    if "category" in kwargs:
        expenseRecord.category = kwargs["category"]
    if "subcategory" in kwargs:
        expenseRecord.subcategory = kwargs["subcategory"]
    if "source" in kwargs:
        expenseRecord.source = kwargs["source"]
    if "goalFk" in kwargs:
        expenseRecord.FK_expense_goal = kwargs["goalFk"]
    if "note" in kwargs:
        expenseRecord.note = kwargs["note"]
    if "ts" in kwargs:
        expenseRecord.ts = kwargs["ts"]

    print(expenseRecord.ammount)
    print(expenseRecord.category)
    print(expenseRecord.subcategory)
    print(expenseRecord.FK_expense_goal)
    print(expenseRecord.note)
    print(expenseRecord.ts)

    db.session.commit()


def delete_expenses_record(recordId):
    expenseRecord = Expense.query.filter_by(_id=recordId).first()
    if expenseRecord is None:
        print(f"Expense record with ID={recordId} not found")
        return
        
    db.session.delete(expenseRecord)
    db.session.commit()


################### GOALS ###################
def add_goal_record(name, targetAmmount, currentAmmount, deadline, ts, note=None):
    goal = Goal(name=name, targetAmmount=targetAmmount, currentAmmount=currentAmmount,
                  deadline=deadline, note=note, ts=ts)
    db.session.add(goal)
    db.session.commit()


def update_goal_record(recordId, **kwargs):
    goalRecord = Goal.query.filter_by(_id=recordId).first()
    if goalRecord is None:
        print(f"Goal record with ID={recordId} not found")
        return
    
    if "name" in kwargs:
        goalRecord.name = kwargs["name"]
    if "targetAmmount" in kwargs:
        goalRecord.targetAmmount = kwargs["targetAmmount"]
    if "currentAmmount" in kwargs:
        goalRecord.currentAmmount = kwargs["currentAmmount"]
    if "deadline" in kwargs:
        goalRecord.deadline = kwargs["deadline"]
    if "note" in kwargs:
        goalRecord.note = kwargs["note"]
    if "ts" in kwargs:
        goalRecord.ts = kwargs["ts"]

    print(goalRecord.name)
    print(goalRecord.targetAmmount)
    print(goalRecord.currentAmmount)
    print(goalRecord.deadline)
    print(goalRecord.note)
    print(goalRecord.ts)

    db.session.commit()


def delete_goal_record(recordId):
    goalRecord = Goal.query.filter_by(_id=recordId).first()
    if goalRecord is None:
        print(f"Goal record with ID={recordId} not found")
        return
        
    db.session.delete(goalRecord)
    db.session.commit()