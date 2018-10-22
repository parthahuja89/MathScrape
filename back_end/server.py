from flask import Flask, jsonify, request
import solo
import os 
from flask_cors import CORS, cross_origin


app = Flask(__name__)
app.config.from_object(__name__)

           
CORS(app) #different origins 
app.config['CORS_HEADERS'] = 'Content-Type'

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response


@app.route('/', methods = ['GET'])
def front():
    print('Hello Wold!')
    return 'yaya'

#reqquests 
@app.route('/send_url', methods=['POST', 'OPTIONS'])
def ping_pong():
     if request.method == 'POST':
         response = request.get_json()
         url = response.get('url')
         tag = reponse.get('tag') 
         css_selector = reponse.get('css_selector')
         print(url)
         soup =solo.setup(url , css_selector)
         #running scrapers 
         solo.scrape_a(soup)
         solo.scrape_1(soup)
         solo.scrape_ord(soup,tag)
         print(solo.getValues())
         print(url)


     return jsonify(solo.getValues())


if __name__ == '__main__':
    app.run()
