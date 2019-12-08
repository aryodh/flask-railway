from flask import Flask, render_template, redirect, jsonify
import os
import time
from multiprocessing import Process
import coba

val = [0]

thrd = []

app = Flask(__name__)

@app.route('/')
def control():
	return render_template('index.html')

def kill():
	while thrd:
		thrd.pop(0).terminate()

@app.route('/open')
def open():
	kill()
	print("open")
	gate = coba.openGate(True)
	coba.offLED()
	add_thrd()
	return jsonify(
		data="success"
	)


@app.route('/close')
def close():
	kill()
	print("close")
	coba.onLED()
	gate = coba.closeGate(False)
	time.sleep(2)
	add_thrd()
	return jsonify(
		data="success"
	)

def auto():
	print("auto")
	coba.main()

def add_thrd():
	print("sesuatu")
	thrd.append(Process(target=auto))
	thrd[0].start()

if __name__ == '__main__':
	add_thrd()
	print(thrd)
	print("masuk1")
	app.run(host='0.0.0.0', port=9999, threaded=True, debug=True, use_reloader=False)
