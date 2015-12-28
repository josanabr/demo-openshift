import os
import pymysql
import datetime, time
from flask import Flask
app = Flask(__name__)
from flask.ext.sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['OPENSHIFT_MYSQL_DB_URL'] + os.environ['OPENSHIFT_APP_NAME']
db = SQLAlchemy(app)

class Event(db.Model):
	#id = db.Column(db.Integer, primary_key = True)
	#username = db.Column(db.String(80), unique = True)
	email = db.Column(db.String(120), unique = False)
	event = db.Column(db.String(512), unique = False)
	id = db.Column(db.String(32), unique = False)

	def __init__(self, id, email, event):
		#self.username = username
		self.email = email
		self.event = event
		self.id = id

	def __repr__(self):
		#return '<User %r> <Event %r>' % (self.username, self.event)
		return '<email %r> <Event %r>' % (self.email, self.event)

app.config['PROPAGATE_EXCEPTIONS'] = True

@app.route("/")
def index():
	events = []
	for event in Event.query.all():
		events.append('{e.id}: <strong>{e.email}'.format(e = event))
	return '<br>'.join(events)
	#return "Hello, code monkey!"
	#return cur.description

@app.route("/createdummy")
def createdummy():
	x=time.mktime(datetime.datetime.now().timetuple())
	e = Event(event = "ls -l", email = "john.sanabria@gmail.com", id = str(x))
	db.session.add(e)
	db.session.commit()
	return "OK"

@app.route("/manrique")
def hola():
	return "Hola, manrique"

if __name__ == "__main__":
	db.create_all()
	for name in ['admin', 'guest']:
		user = Events(name, '%s@demo.org'%name)
		db.session.add(user)
	db.session.commit()
	app.run()

