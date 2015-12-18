import os
import pymysql
from flask import Flask
app = Flask(__name__)
from flask.ext.sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['OPENSHIFT_MYSQL_DB_URL']
db = SQLAlchemy(app)

class Event(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(80), unique = True)
	email = db.Column(db.String(120), unique = False)

	def __init__(self, username, email):
		self.username = username
		self.email = email

	def __repr__(self):
		return '<User %r>' % self.username

app.config['PROPAGATE_EXCEPTIONS'] = True

@app.route("/")
def index():
	users = []
	for user in User.query.all():
		users.appen('{u.id}: <strong>{u.username}'.format(u = user))
	return '<br>'.join(users)
	#return "Hello, code monkey!"
	#return cur.description

if __name__ == "__main__":
	app.run()
