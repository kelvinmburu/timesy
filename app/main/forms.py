from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField, SelectField
from wtforms.validators import InputRequired

class TaskForm(FlaskForm):

    task = TextAreaField(label='',validators=[InputRequired()], render_kw={"placeholder": "Add Task"})
    submit = SubmitField('Submit')

class ReminderForm(FlaskForm):

    emails = TextAreaField(label='',validators=[InputRequired()], render_kw={"placeholder": "Add email"})
    submit = SubmitField('Submit')