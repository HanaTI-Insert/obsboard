#!/usr/bin/python
from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests
app = Flask(__name__)
@app.route("/")
def main():
	r = requests.get('https://loahae.com/')
	soup = BeautifulSoup(r.text, 'html.parser')
	data = soup.find('div', {'class':'content'})
        return render_template('index.html', content=unicode(data))
	#return '<!DOCTYPE html><head><meta charset="utf-8"><link href="https://loahae.com/assets/css/loahae.css" rel="stylesheet"></head><body class="main"></br>%s<meta http-equiv="refresh" content="600; URL=/"></body></html>' % str(data)
app.run(host='0.0.0.0', debug=True)
