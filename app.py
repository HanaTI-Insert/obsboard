from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)
@app.route("/")
def main():
	r = requests.get('https://loahae.com/')
	soup = BeautifulSoup(r.text, 'html.parser')
	mari = soup.find('div', {'class':'box mari'})
	print type(mari)
	return '<html><head><link href="https://loahae.com/assets/css/loahae.css" rel="stylesheet"></head><body>'+str(mari)+'</body></html>'
	#return 'test'
app.run(host='0.0.0.0', debug=True)
