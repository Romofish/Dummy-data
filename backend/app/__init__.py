from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

from app.api import routes

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
