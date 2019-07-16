"""
    run server: python3 main.py
    the target modle.json file is at http://localhost:5000/models/mnist/model.json
"""
from flask import Flask
from flask_cors import CORS

app = Flask(__name__,
            static_url_path='/models', 
            static_folder='models')

cors = CORS(app) 

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run(debug=True)