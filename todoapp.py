from flask import Flask, render_template, request, redirect, url_for
from flask.ext.bootstrap import Bootstrap
from forms import Entry
from flask_wtf.csrf import CsrfProtect
from models import db, Item


app = Flask(__name__)
bootstrap = Bootstrap(app)
db.init_app(app)
csrf = CsrfProtect(app)


app.config['SECRET_KEY'] = "string"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:dog@localhost/todoapp'

@app.route('/', methods = ['GET', 'POST'])
def todo():
	entry = Entry()

	if request.method =='POST':
		new_item = Item(item = entry.to_do.data)
		db.session.add(new_item)
		db.session.commit() 
		print "shit worked"
		return redirect(url_for('show'))


	return render_template("index.html", form = entry)

@app.route('/show')
def show():
	all_items = Item.query.all()

	return render_template('show.html', object = all_items)


@app.route('/show_reverse/')
def show_reverse():
	all_items = Item.query.order_by(Item.item_id.desc()).all()

	return render_template('show_reverse.html', object = all_items)


@app.route('/<int:item_id>/edit/', methods = ['GET', 'POST'])
def editItem(item_id):
	editedItem = Item.query.filter_by(item_id = item_id).one()
	if request.method == 'POST':
		if request.form['name']:
			editedItem.item = request.form['name']
			print type(editedItem)
			print editedItem
		db.session.add(editedItem)
		db.session.commit()
		return redirect(url_for('show'))


	else:
		return render_template('edit_item.html', i = editedItem)



@app.route('/<int:item_id>/delete/', methods = ['GET', 'POST'])
def deleteItem(item_id):

	deletedItem = Item.query.filter_by(item_id = item_id).one()
	if request.method == 'POST':
		db.session.delete(deletedItem)
		db.session.commit()
		return redirect(url_for('show'))


	else:
		return render_template('delete_item.html', i = deletedItem)





if __name__ == '__main__':
	app.debug = True
	app.run()