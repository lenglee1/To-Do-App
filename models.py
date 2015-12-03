from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Item(db.Model):
	__tablename__ = 'Items'

	item_id = db.Column(db.Integer, primary_key = True)
	item = db.Column(db.Text)
	uploaded_file = db.Column(db.Text)





