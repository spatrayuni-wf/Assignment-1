from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def index():
    ATC_USERNAME = os.environ.get('ATC_USERNAME')
    ATC_PASSWORD = os.environ.get('ATC_PASSWORD')
    return  'ATC_USERNAME: {} ATC_PASSWORD:{}'.format(ATC_USERNAME, ATC_PASSWORD)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)