from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField, SelectField
from wtforms.validators import InputRequired

class TaskForm(FlaskForm):

    task = TextAreaField('Blog review', validators=[InputRequired()])
    submit = SubmitField('Submit')