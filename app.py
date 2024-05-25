from flask import Flask
import psycopg2
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/db')
def db():
    conn = psycopg2.connect(host='DB',
                            database='flask_db',
                            user=os.environ['pguser'],
                            password=os.environ['pgpass'])

    cur = conn.cursor()
    cur.execute("""
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = 'public'
    """)
    table_names = cur.fetchall()
    return "".join("<p>Table name: {}</p>".format(t) for t in table_names)

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')
