from flask import Flask, jsonify, request
import scraper
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
         soup =scraper.setup(url)
         #running scrapers 
         scraper.scrape_a(soup)
         scraper.scrape_1(soup)
         scraper.scrape_ord(soup)
         print(scraper.getValues())
         print(url)


     return jsonify(scraper.getValues())


if __name__ == '__main__':
    app.run()
