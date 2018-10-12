from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
app.config.from_object(__name__)

           
CORS(app) #different origins 


#reqquests 
@app.route('/send_url', methods=['POST', 'GET'])
def ping_pong():
     if request.method == 'POST':
         response = request.get_json()
         url = response.get('url')
         print(url)


     return jsonify('url received')


if __name__ == '__main__':
    app.run()
