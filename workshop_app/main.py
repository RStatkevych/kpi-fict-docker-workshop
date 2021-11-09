import psycopg2
from flask import Flask, send_file

app = Flask(__name__)


@app.route("/dogge")
def dogge_endpoint():
    return send_file('../img/dogge.jpg', mimetype='image/jpeg')


@app.route("/db")
def db_endpoint():
    conn = psycopg2.connect("host=database dbname=test user=postgres password=S0meP@ssw0rd")
    cursor = conn.cursor()
    cursor.execute("SELECT counter FROM counter");
    counter_value = cursor.fetchone()[0]
    resp = f"<p>You visited this page {counter_value + 1} times!</p>"
    cursor.execute("UPDATE counter SET counter=%s WHERE counter=%s",
                   (counter_value + 1, counter_value))
    conn.commit()
    cursor.close()
    conn.close()
    return resp


app.run(host='0.0.0.0', port=7777)
