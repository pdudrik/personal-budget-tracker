from app import db


class Income(db.Model):
    __tablename__ = "Income"
    _id = db.Column("id", db.Integer, primary_key=True)
    ammount = db.Column(db.Numeric(6,2), nullable=False)
    currency = db.Column(db.String(1), nullable=False, default="EUR")
    source = db.Column(db.String(30),nullable=False)
    note = db.Column(db.String(100))
    ts = db.Column(db.Date)

    def __repr__(self):
        return f"Income({self._id}, {self.source})"


class Expense(db.Model):
    __tablename__ = "Expense"
    _id = db.Column("id", db.Integer, primary_key=True)
    ammount = db.Column(db.Numeric(7,2), nullable=False)
    currency = db.Column(db.String(1), nullable=False, default="EUR")
    category = db.Column(db.String(50), nullable=False)
    subcategory = db.Column(db.String(50), nullable=False)
    note = db.Column(db.String(100))
    ts = db.Column(db.Date, nullable=False)
    FK_expense_goal = db.Column(db.Integer, db.ForeignKey("Goal.id"), default=None)


class Goal(db.Model):
    __tablename__ = "Goal"
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    targetAmmount = db.Column(db.Numeric(8,2), nullable=False)
    currentAmmount = db.Column(db.Numeric(8,2), nullable=False)
    currency = db.Column(db.String(1), nullable=False, default="EUR")
    deadline = db.Column(db.Date)
    note = db.Column(db.String(100))
    expenses = db.relationship("Expense", backref="goal") 
