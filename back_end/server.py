from flask import Flask, jsonify, request
import solo
from flask_cors import CORS


app = Flask(__name__)
app.config.from_object(__name__)

           
CORS(app) #different origins 

@app.route('/', methods = ['GET'])
def front():
    print('Hello Wold!')
#reqquests 
@app.route('/send_url', methods=['POST', 'GET', 'OPTIONS'])
def ping_pong():
     if request.method == 'POST, OPTIONS':
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
