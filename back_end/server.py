from flask import Flask, jsonify, request
import solo
from flask_cors import CORS, cross_origin


app = Flask(__name__)
app.config.from_object(__name__)

           
CORS(app) #different origins 
app.config['CORS_HEADERS'] = 'Content-Type'
@app.route('/', methods = ['GET'])
def front():
    print('Hello Wold!')
    return 'yaya'

#reqquests 
@app.route('/send_url', methods=['POST', 'GET'])
@cross_origin()
def ping_pong():
     if request.method == 'POST':
         response = request.get_json()
         url = response.get('url')
         soup =solo.setup(url)
         #running scrapers 
         solo.scrape_a(soup)
         solo.scrape_1(soup)
         solo.scrape_ord(soup)
         print(solo.getValues())
         print(url)


     return jsonify(solo.getValues())


if __name__ == '__main__':
    app.run()
