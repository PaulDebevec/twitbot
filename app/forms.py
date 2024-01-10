# app/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class BotPostForm(FlaskForm):
    part_one = StringField('Part One')
    part_two = StringField('Part Two')
    submit = SubmitField('Create BotPost')

class BulkCreateForm(FlaskForm):
    botposts_json = TextAreaField('BotPosts JSON', validators=[DataRequired()])
    submit = SubmitField('Bulk Create BotPosts')