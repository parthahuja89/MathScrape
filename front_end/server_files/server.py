from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)
app.config.from_object(__name__)

           
CORS(app) #different origins 


#reqquests 
@app.route('/send_url', methods=['POST'])
def ping_pong():
     print(request.json())
     return jsonify('url received')


if __name__ == '__main__':
    app.run()
