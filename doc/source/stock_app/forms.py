from wtforms import TextField
from wtforms.fields import SubmitField
from wtforms.validators import DataRequired
from flask.ext.wtf import Form

class SymbolSearch(Form):
    symbol = TextField('Symbol', validators=[DataRequired,])
    trend1 = TextField('Trend 1', validators=[DataRequired,])
    trend2 = TextField('Trend 2', validators=[DataRequired,])
    submit = SubmitField('Search')