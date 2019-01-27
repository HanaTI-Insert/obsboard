#!/usr/bin/python
from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests
app = Flask(__name__)
@app.route("/")
def main():
    soup = BeautifulSoup(requests.get('https://loahae.com/').text, 'html.parser')
    m = soup.find('div', {'class':'box mari'})
    c = soup.find('div', {'class':'box calendar'})
    return render_template('index.html', mari=unicode(m), calendar=unicode(c))
app.run(host='0.0.0.0', debug=True)
