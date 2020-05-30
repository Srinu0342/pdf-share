from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField

class registration(FlaskForm):
    name=StringField('Name')
    email=StringField('email')
    submit=SubmitField('register')
