from flask import Flask,request
from flask import jsonify
app = Flask(__name__)

@app.route('/summary')
def summary():
    return jsonify (
        title="Twitter",
        text="@TorbenWetter hat deinen Tweet geliked!",
        time="19:52:35"
    )     
    

#def hello_world():
#    return 'Hello, World!'

@app.route('/receiver', methods=["POST"]) 
def receiver():
    #print(request.args["param"])
    #print(request.form["param1"])
    return jsonify (
        success=True,
        failure=False,
        #channel=channel,
        #anfrage=request.get_json(force=true)
        #param2=request.args["param2"],
        title=request.form["param1"],
        text=request.form["param2"],
        time=request.form["param3"]
    )