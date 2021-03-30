from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SubmitField, BooleanField
import email_validator
from wtforms.validators import DataRequired,Email,Length,EqualTo

class registration(FlaskForm):
    username=StringField("Username",validators=[DataRequired(),Length(min=2,max=15)])
    email= StringField("Email",validators=[DataRequired(),Email()])
    password= PasswordField("password",validators=[DataRequired()])
    confirm= PasswordField('confirm your password',validators=[DataRequired(),EqualTo("password")])
    submit=SubmitField("submit")


class Login(FlaskForm):
    email= StringField("Email",validators=[DataRequired(),Email()])
    password= PasswordField("password",validators=[DataRequired()]) 
    remember_me=BooleanField("Remember me")
    login=SubmitField("Sign in")