#!/usr/bin/python
#-*- coding: utf-8 -*-
from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests, time
app = Flask(__name__)
@app.route("/")
def main():
    soup = BeautifulSoup(requests.get('https://loahae.com/').text, 'html.parser')
    m = soup.find('div', {'class':'box mari'})
    c = soup.find('div', {'class':'box calendar'})
    return render_template('index.html', mari=unicode(m), calendar=unicode(c))
@app.route('/endy')
def endy():
    t = {0:'루테란', 1:'슈테른', 2:'베른', 3:'페이토', 4:'아트로포스', 5:'로헨델', 6:'루테란', 7:'슈테른', 8:'베른', 9:'페이토', 10:'아트로포스', 11:'로헨델', 12:'루테란', 13:'슈테른', 14:'베른', 15:'페이토', 16:'아트로포스', 17:'로헨델', 18:'루테란', 19:'슈테른', 20:'베른', 21:'페이토', 22:'아트로포스', 23:'로헨델'}
    return render_template('endy.html', town=t[time.localtime().tm_hour].decode('utf-8'))
app.run(host='0.0.0.0', debug=True)

