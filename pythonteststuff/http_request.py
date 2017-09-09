from flask import Flask,request
from flask import jsonify
import sqlite3
app = Flask(__name__)


sqlite_file = 'always_on_db.sqlite'


table_name = 'notifications'
 #title=request.form["title"],
        #text=request.form["text"],
        #time=request.form["time"]



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
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    title = request.form["title"]
    text = request.form["text"]
    time = request.form["time"]
    id_column = "title"
    column_name1 = "text"
    column_name2 = "time"
    
    try:
        sql = 'INSERT INTO {tn} ({idf}, {cn1}, {cn2}) VALUES ("{title}", "{text}", "{time}")'.\
        format(tn=table_name, idf=id_column, title=title, text=text, time=time, cn1=column_name1, cn2=column_name2)
        print(sql)
        c.execute(sql)
    except sqlite3.IntegrityError:
        print('ERROR: ID already exists in PRIMARY KEY column {}'.format(id_column))



    conn.commit()
    #conn.close()
@app.route('/sender', methods=["GET"])
def sender():
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    title = request.form["title"]
    text = request.form["text"]
    time = request.form["time"]
    
    

    sql = "SELECT * FROM {tn} ORDER BY {time} DESC LIMIT 10" .\
    format(tn=table_name, time=time)
    print(sql)
    c.execute(sql)
    ''' return jsonify (

        #channel=channel,
        #anfrage=request.get_json(force=true)
        #param2=request.args["param2"],
        title=request.form["title"],
        text=request.form["text"],
        time=request.form["time"]
    )'''