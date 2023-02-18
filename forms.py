from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, SelectField
from wtforms.validators import InputRequired, Optional, URL, NumberRange, AnyOf

class CupcakeForm(FlaskForm):
    flavor = StringField('Flavor', validators=[InputRequired(message='Cant be blank')])
    size = StringField('Size', validators=[InputRequired(message='Enter a size'), AnyOf(values=['small', 'medium', 'large'], message='small, medium, or large')])
    rating = FloatField('Enter Rating', validators=[InputRequired(message='Enter a rating')])
    image = StringField('Image URL', validators=[URL(message='Must be a URL'), Optional()])