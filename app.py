from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('scenarios.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/scenarios', methods=['GET'])
def get_scenarios():
    conn = get_db_connection()
    scenarios = conn.execute('SELECT * FROM scenarios').fetchall()
    conn.close()
    return jsonify([dict(row) for row in scenarios])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
