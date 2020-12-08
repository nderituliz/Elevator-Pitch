from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class PitchForm(FlaskForm):
    content = TextAreaField('Post your Elevator Pitch',validators=[Required()])
    submit = SubmitField('Submit')