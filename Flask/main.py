#!usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template
from flask import request
from flask_wtf import CsrfProtect
import forms
import json

app = Flask(__name__)
app.secret_key = 'my_secret_key'

@app.route('/')
def index():	
	data = {"api":"rest :)"}
	return json.dumps(data)

@app.route('/auth/login', methods = ['POST'])
def log_auth():
	values = request.get_json()
	if values['usuario'] == 'admin' and values['clave'] == 'top_secret':
		respuesta = {'error':True, 'mensaje':'Auser logged'}
		return json.dumps(respuesta)
	respuesta = {'error':True,'mensaje':'Fail Auth'}
	return json.dumps(values)

@app.route('/app/api/post', methods=['GET'])
def api_post():
	data = []
	
	for i in range(10):
		
		data.append({
			"titulo":"titulo",
			"detalles":"Cualquier texto solo para comprobar si se escribe o no",
			"tags":["android","nodejs","javascript"]
		})
	return json.dumps(data)

@app.route('/app/api/post//', methods = ['GET'])
def details_post(id):
	data = {
		"titulo":"titulo {} ".format(id),
		"detalles":"Cualquier texto solo para comprobar si se escribe o no",
		"tags":["android","nodejs","javascript"]
	}
	return json.dumps(data)
	
if __name__ == '__main__':
	app.run(debug=True, port=8888)