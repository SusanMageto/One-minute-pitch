from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,SubmitField,TextAreaField,RadioField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError



class PitchForm(FlaskForm):
	title = StringField('Title', validators=[DataRequired()])
	description = TextAreaField("Pitch Idea",validators=[DataRequired()])
	category = RadioField('Label', choices=[('movies','movies'), ('music','music'), ('art','art'),('general','general')],validators=[DataRequired()])
	submit = SubmitField('Submit')

class CommentForm(FlaskForm):
	description = TextAreaField('Add your comments here!',validators=[DataRequired()])
	submit = SubmitField('Add')



class UpvoteForm(FlaskForm):
	submit = SubmitField('Submit')


class Downvote(FlaskForm):
	submit = SubmitField('Submit')