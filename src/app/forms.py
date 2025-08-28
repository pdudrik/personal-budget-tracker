from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, IntegerField, FloatField, SelectField
from wtforms.validators import DataRequired
from app.config import SOURCE_CHOICES, CATEGORY_CHOICES, SUBCATEGORY_CHOICES


class IncomeForm(FlaskForm):
    ammount = FloatField("Enter ammount", validators=[DataRequired()])
    source = SelectField("Source of income", choices=SOURCE_CHOICES, default=None, validators=[DataRequired()])
    ts = DateField("Date of receivement", validators=[DataRequired()])
    note = StringField("Description")
    submit = SubmitField("Submit")
    update = SubmitField("Update")


class ExpensesForm(FlaskForm):
    ammount = FloatField("Enter ammount", validators=[DataRequired()])
    ts = DateField("Date of receivement", validators=[DataRequired()])
    category = SelectField("Category", choices=CATEGORY_CHOICES, default=None, validators=[DataRequired()])
    subcategory = SelectField("Subcategory", choices=SUBCATEGORY_CHOICES, default=None, validators=[DataRequired()])
    note = StringField("Description")
    submit = SubmitField("Submit")
    update = SubmitField("Update")