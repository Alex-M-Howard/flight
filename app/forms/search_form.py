from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo

class SearchForm(FlaskForm):
    from_city = StringField('From', validators=[DataRequired()])
    to_city = StringField('To')
    date_from = StringField('Date From', validators=[DataRequired()])
    date_to = StringField('Date To', validators=[DataRequired()])
    nights_in_dst_from = StringField('Nights in Destination From')
    nights_in_dst_to = StringField('Nights in Destination To')
    flight_type = StringField('Flight Type')
    curr = StringField('Currency')
    price_from = StringField('Price From')
    price_to = StringField('Price To')