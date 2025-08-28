from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, IntegerField, FloatField, SelectField
from wtforms.validators import DataRequired
from app.config import choices


class IncomeForm(FlaskForm):
    ammount = FloatField("Enter ammount", validators=[DataRequired()])
    source = SelectField("Source of income", choices=choices, default=None, validators=[DataRequired()])
    ts = DateField("Date of receivement", validators=[DataRequired()])
    note = StringField("Description")
    submit = SubmitField("Submit")
    update = SubmitField("Update")