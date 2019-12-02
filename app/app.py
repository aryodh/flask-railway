from flask import Flask, render_template
from celery import Celery
import celeryApp
import os

app = Flask(__name__)

app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379',
    CELERY_RESULT_BACKEND='redis://localhost:6379'
)

celeryApps = celeryApp.make_celery(app)

@app.route('/')
def control():
	return render_template('index.html')


@celeryApps.task()
def railway():
	print("kepanggil")

if __name__ == '__main__':
	print("masuk")
	result = railway.delay()
	print("masuk1")
	print("masuk2")
	app.run(host='0.0.0.0', port=9999, threaded=True, debug=True)
