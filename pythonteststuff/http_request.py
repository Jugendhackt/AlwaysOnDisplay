from flask import Flask, request
from flask import jsonify
import sqlite3

app = Flask(__name__)

sqlite_file = 'always_on_db.sqlite'

table_name = 'notifications'


@app.route('/receiver', methods=["POST"])
def receiver():
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    print("connection")

    if 'time' not in request.form or 'text' not in request.form or 'title' not in request.form:
        print("no success")
        return jsonify(success=False)

    time_value = request.form["time"]
    text_value = request.form["text"]
    title_value = request.form["title"]

    id_column_primary = "time"
    column_text = "text"
    column_title = "title"

    try:
        sql = 'INSERT INTO {tn} ({idf}, {cn1}, {cn2}) VALUES ("{timev}", "{txtv}", "{tv}")'. \
            format(tn=table_name, idf=id_column_primary, cn1=column_text, cn2=column_title, txtv=text_value,
                   timev=time_value, tv=title_value)
        print(sql)
        c.execute(sql)
    except sqlite3.IntegrityError:
        print('ERROR: ID already exists in PRIMARY KEY column {}'.format(id_column_primary))

    conn.commit()

    print("success")
    return jsonify(
        success=True,
        title=title_value,
        text=text_value,
        time=time_value
    )


@app.route('/sender', methods=["GET"])
def sender():
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    id_column_primary = "time"

    sql = "SELECT * FROM {tn} ORDER BY {time} DESC LIMIT 10". \
        format(tn=table_name, time=id_column_primary)
    c.execute(sql)
    all_rows = c.fetchall()
    print('1):', all_rows)
    return jsonify(
        text=all_rows[0][0],
        title=all_rows[0][1],
        time=all_rows[0][2],
        ok=True
    )
