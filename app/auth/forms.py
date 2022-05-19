from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired,Email,EqualTo,Length
from flask_bootstrap import Bootstrap
from ..models import User
from wtforms import ValidationError

class RegistrationForm(FlaskForm):
    email = StringField('Your Email Address',validators=[DataRequired(),Email()])
    username = StringField('Enter your username',validators = [DataRequired()])
    password = PasswordField('Password',validators = [DataRequired(), EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Password',validators = [DataRequired()])
    submit = SubmitField('Sign Up')
    
    def validate_email(self,data_field):
        if User.query.filter_by(email =data_field.data).first():
            raise ValidationError('There is an account with that email')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken')

class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(min=6, max=100)])
    password = PasswordField('password', validators=[DataRequired(), Length(min=8, max=80)])
    rememberMe = BooleanField('remember me')
    