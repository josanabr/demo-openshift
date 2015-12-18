import os
import pymysql
from flask import Flask
app = Flask(__name__)

app.config['PROPAGATE_EXCEPTIONS'] = True
@app.route("/")
def insult():
	conn = pymysql.connect(host = os.environ['OPENSHIFT_MYSQL_DB_HOST'], port=os.environ['OPENSHIFT_MYSQL_DB_PORT'], user=os.environ['OPENSHIFT_MYSQL_DB_USERNAME'], passwd=os.environ['OPENSHIFT_MYSQL_DB_PASSWORD'], db=os.environ['OPENSHIFT_MYSQL_DB_URL'])
	cur = conn.cursor()
	cur.execute("Select * from events")
	#return "Hello, code monkey!"
	return cur.description
if __name__ == "__main__":
	app.run()
