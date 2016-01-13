import os
import pymysql
import datetime, time
from flask import Flask, request
app = Flask(__name__)
from flask.ext.sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['OPENSHIFT_MYSQL_DB_URL'] + os.environ['OPENSHIFT_APP_NAME']
db = SQLAlchemy(app)

class Event(db.Model):
	idprimary = db.Column(db.Integer, primary_key = True)
	__tablename__ = 'event'
	email = db.Column(db.String(120), unique = False)
	event0 = db.Column(db.String(512), unique = False)
	datetime = db.Column(db.String(32), unique = False)

	def __init__(self, datetime, email, event0):
		#self.username = username
		self.email = email
		self.event0 = event0
		self.datetime = datetime

	def __repr__(self):
		return '<email %r> <Event %r>' % (self.email, self.datetime)

app.config['PROPAGATE_EXCEPTIONS'] = True

@app.route("/")
def index():
#	events = []
#	for event in Event.query.all():
#		events.append('{e.idprimary} -- {e.datetime}: <strong>{e.email}</strong>: {e.event0}'.format(e = event))
#	return '<br>'.join(events)
    return "Edier"

@app.route("/createdummy")
def createdummy():
	x=time.mktime(datetime.datetime.now().timetuple())
	e = Event(event0 = "ls -l", email = "john.sanabria@gmail.com", datetime = str(x))
	db.session.add(e)
	db.session.commit()
	return "OK"

@app.route("/addevent", methods=['POST'])
def addevent():
	x = time.mktime(datetime.datetime.now().timetuple())
	e = Event(event0 = request.form['event0'], email = request.form['email'], datetime = str(x))
	db.session.add(e)
	db.session.commit()
	return "OK"

@app.route("/getlasttemperature", methods=['GET'])
def querylasttemperature(): 
#    events = []
#    for event in Event.query.all():
#            events.append('{e.idprimary}#{e.datetime}#\
#                    <strong>{e.event0}</strong>'.format(e = event))
    events = gettemperaturelist()
    return events[len(events) - 1]

@app.route("/gettemperature", methods=['POST'])
def querytemperature(): 
    events = []
#    for event in Event.query.all():
#            events.append('{e.idprimary} {e.datetime} \
#                    <strong>{e.event0}</strong>'.format(e = event))
    return events[len(events) - 1]

def gettemperaturelist():
    events = []
    for event in Event.query.all():
            events.append('{e.idprimary}#{e.datetime}#\
                    <strong>{e.event0}</strong>'.format(e = event))
    return events
	
if __name__ == "__main__":
	db.create_all()
	for name in ['admin', 'guest']:
		user = Events(name, '%s@demo.org'%name)
		db.session.add(user)
	db.session.commit()
	app.run()

