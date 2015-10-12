import os
from flask import Flask
app = Flask(__name__)

app.config['PROPAGATE_EXCEPTIONS'] = True
@app.route("/")
def insult():
	return "Hello, code monkey!"
if __name__ == "__main__":
	app.run()
