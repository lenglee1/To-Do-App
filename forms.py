from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, FileField, TextAreaField

class Entry(Form):
	to_do = TextAreaField("Please enter your to do item:")
	image = FileField("Please upload an image associated with your to do item: ")

	submit = SubmitField("Submit")

