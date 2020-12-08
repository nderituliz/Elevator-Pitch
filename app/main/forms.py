from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class PitchForm(FlaskForm):
    content = TextAreaField('Post your Elevator Pitch',validators=[Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    opinion = TextAreaField('Post your Comment')
    submit = SubmitField('Submit')

class CategoryForm(FlaskForm):
    name = StringField('Category Name', validators=[Required()])
    submit = SubmitField('Create')