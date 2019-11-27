from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
	text = compilation()
	return text

def compilation():
	print("masuk")
	return "ini masuk"

@app.route('/control')
def control():
	return render_template('index.html')
