from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class RegistrationForm(FlaskForm):
    userName = StringField('Username', validators=[])

