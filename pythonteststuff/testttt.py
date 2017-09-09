from flask import Flask
from flask import jsonify
app = Flask(__name__)

@app.route('/summary')
def summary():
    return jsonify (
        apptitle="Twitter",
        appcontent="@TorbenWetter hat deinen Tweet geliked!"
    )     
    

#def hello_world():
#    return 'Hello, World!'

